# BitREAPER - Secure & Embeddable solution for data sanitization

## The Problem (2025 SIH Problem Statement \#SIH25070)
India is facing a growing e-waste crisis, generating over 1.75 million tonnes annually. A key reason why millions of old laptops and smartphones remain unused or improperly discarded is fear of data breaches. Most users hesitate to recycle their devices due to concerns about sensitive personal or organizational data being recovered. Existing data sanitization tools are either too complex, expensive, or lack verifiable proof of erasure. This gap has led to over ₹50,000 crore worth of IT assets being hoarded in homes and offices, hindering circular economy efforts. A user-friendly, tamper-proof, and auditable data wiping solution is urgently needed to promote safe disposal and reuse of electronic devices.

## The Solution
BitREAPER :
* Is a bootable USB tool for secure and irreversible disk erasure.
* Runs independent of host OS which gives full control of wipe process.
* Is compliant with NIST SP 800-88 media sanitization guidelines.
* Uses trusted open-source utilities (nwipe, hdparm, nvme-cli).
* Verification utility (testdisk) ensures wipe success.
* Generates digitally signed, tamper-proof wipe certificate.
* Simple UI helps non-technical users operate the program easily.
* Low-cost and portable, powered by FOSS tools.

![program flowchart](https://github.com/sayujya-apte/BitREAPER/blob/2c6f9720930ccbec2e1b0bddddb6c5bc240a752e/fc2.png)
