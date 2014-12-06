import subprocess
import os
import ephem
import time

print "Initializing"

workingDirectory = os.path.dirname(os.path.realpath(__file__))
os.chdir(workingDirectory) # Set script directory as working directory

# ------ Satellite info ------
tleISS = ["ISS",
    "1 25544U 98067A   14339.58461381  .00016717  00000-0  10270-3 0  9003",
    "2 25544  51.6433 329.7510 0007310  97.8404 262.3577 15.51823685 37921"]
ISS = ephem.readtle(tleISS[0], tleISS[1], tleISS[2])

tleTiangong1 = ["Tiangong 1",
    "1 37820U 11053A   14340.11779331  .00045223  00000-0  47422-3 0  6371",
    "2 37820 042.7707 354.7642 0017103 252.3073 154.5521 15.63444670183054"]
tiangong1 = ephem.readtle(tleTiangong1[0], tleTiangong1[1], tleTiangong1[2])

tleHubble = ["HST",
    "1 20580U 90037B   14338.63623843  .00004206  00000-0  26736-3 0  1708",
    "2 20580 028.4717 356.0619 0002784 311.0334 343.8095 15.06330269150432"]
hubble = ephem.readtle(tleHubble[0], tleHubble[1], tleHubble[2])

# ------ Images info ------
issImage = "iss.png"
issImageOriginX = 47
issImageOriginY = 26

tiangong1Image = "tiangong1.png"
tiangong1ImageOriginX = 35
tiangong1ImageOriginY = 21

hubbleImage = "hubble.png"
hubbleImageOriginX = 30
hubbleImageOriginY = 27

worldImage = "world.png"
worldImageWidth = 1920
worldImageHeight = 1080

tempImage = "temp.png"
currentImage = 0

# Map info
minLat = -90
minLong = -180
maxLat = 90
maxLong = 180

worldImagePxPerDegreeX = worldImageWidth / (maxLong - minLong)
worldImagePxPerDegreeY = worldImageHeight / (maxLat - minLat)

while True:
    print "Updating..."

    # Create temp image
    subprocess.call("cp " + worldImage + " " + tempImage, shell=True)

    # ------ Calculate satellite position ------

    ISS.compute()
    tiangong1.compute()
    hubble.compute()

    # ------ Draw satellites ------

    x = (ISS.sublong/ephem.degree - minLong) * worldImagePxPerDegreeX - issImageOriginX
    y = -(ISS.sublat/ephem.degree + minLat) * worldImagePxPerDegreeY - issImageOriginY
    satelliteImage = issImage
    subprocess.call("/usr/bin/composite -geometry +" + str(x) + "+" + str(y) + " " + satelliteImage + " " + tempImage + " " + tempImage, shell=True)

    x = (tiangong1.sublong/ephem.degree - minLong) * worldImagePxPerDegreeX - tiangong1ImageOriginX
    y = -(tiangong1.sublat/ephem.degree + minLat) * worldImagePxPerDegreeY - tiangong1ImageOriginY
    satelliteImage = tiangong1Image
    subprocess.call("/usr/bin/composite -geometry +" + str(x) + "+" + str(y) + " " + satelliteImage + " " + tempImage + " " + tempImage, shell=True)

    x = (hubble.sublong/ephem.degree - minLong) * worldImagePxPerDegreeX - hubbleImageOriginX
    y = -(hubble.sublat/ephem.degree + minLat) * worldImagePxPerDegreeY - hubbleImageOriginY
    satelliteImage = hubbleImage
    subprocess.call("/usr/bin/composite -geometry +" + str(x) + "+" + str(y) + " " + satelliteImage + " " + tempImage + " " + tempImage, shell=True)

    # ------ Finish ------

    if (currentImage == 0):
        outImage = "wallpaper/wallpaper1.png"
        oldImage = "wallpaper/wallpaper0.png"
        currentImage = 1
    else:
        outImage = "wallpaper/wallpaper0.png"
        oldImage = "wallpaper/wallpaper1.png"
        currentImage = 0

    subprocess.call("mv " + tempImage + " " + outImage, shell=True) # Rename temporal image to final image

    subprocess.call("rm " + oldImage, shell=True) # Delete previous image

    subprocess.call("xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitoreDP1/workspace0/last-image --set " + workingDirectory + "/" + outImage, shell=True) # Change wallpaper, may vary between computers

    print "Finished"
    time.sleep(30) # Wait 30 seconds
