# Postmortem: Ubuntu Laptop Boot Issue - Jun 9th, 2023

## Issue Summary

From approximately 11:05AM EAT on Jun 9th to 1:40PM Jun 9th, my Ubuntu 22.04 Laptop experienced a boot issue where it booted up to a terminal with no GUI alternative to log into. This prevented graphical access to the laptop, forcing the use of the terminal for all tasks. The issue caused concern and disruption to normal workflow.

## Timeline

`11:05AM-11:20AM:`

**Description:** Attempted to log in repeatedly to access the laptop and start working.

`11:20AM-11:30AM:`

**Description:** Performed system update and package upgrade.
Outcome: System update and package upgrade completed successfully.

`11:30AM-11:40AM:`

**Description:** Checked the log files (/var/log/syslog) to investigate the root cause of the problem.

`11:40AM-12:00PM:`

**Description:** Installed LightDM display manager as a potential solution.
Outcome: The issue persisted even after the installation.

`12:00PM-1:20PM:`

**Description:** Further reviewed the log files to determine the default display manager.

`1:20PM-1:30PM:`

**Description:** Reinstalled a broken GDM3 (GNOME Display Manager) as a replacement.
Outcome: Reinitialized the system and regained GUI display.

`1:30PM-1:40PM:`

**Description:** Reinstalled ubuntu-desktop package to restore necessary packages in the desktop environment.

## Root Cause

The root cause of the issue was the absence of a compatible display manager, preventing the computer from processing and displaying graphics properly. This was traced back to a forced installation of an incompatible package, which resulted in dependency conflicts, package version mismatches, and subsequent disruption and removal of display-related packages.


## Resolution and Recovery

To resolve the issue and recover the graphical interface, the following actions were taken:

* Rolled back the installations of `libglapi-mesa` and `libegl1-mesa0` to compatible versions with the Ubuntu 22.04 system.

* Performed system update and package upgrade to ensure the latest updates and packages were installed.

* Attempted installation of `LightDM` display manager, which was discovered to be incompatible with the system.

* Reinstalled `GDM3` (Gnome Display Manager), the default display manager for Gnome Desktop Environments.

* Reinitialized the system, ensuring the changes took effect.

* Reinstalled the `ubuntu-desktop` package to retrieve all the necessary packages in the desktop environment.

* After these steps, the laptop was restored to its normal functioning state with the GUI display.

## Corrective and Preventative Measures

**Corrective Measures:**

* Always use package versions that are officially supported by the Ubuntu OS release to maintain system stability and compatibility.

* Review log files (/var/log/syslog) to identify the root cause of issues and take appropriate actions.

* Regularly update and upgrade the system to ensure the latest packages and security updates are applied.

**Preventative Measures:**

Verify the compatibility of packages before installation to avoid potential conflicts or dependencies.

Backup important files and configurations regularly to minimize data loss in case of system failures or unexpected issues.

Consider creating system restore points or using version control systems for easy restoration to a working state.

Stay informed about the latest updates, news, and issues related to the operating system to proactively address potential problems.

Have a secondary system or alternative means of accessing work (e.g., secondary device or remote access) to reduce downtime during critical system issues.

By following these measures, system stability and compatibility can be maintained, and the likelihood of similar boot issues can be reduced in the future.
