# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-user-notifications
%global full_version 0.2.2
%global pkgname objc2-user-notifications-0.2

Name:           rust-objc2-user-notifications-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-user-notifications"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:76cfcbf642358e8689af64cee815d139339f3ed8ad05103ed5eaf73db8d84cb3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unnotificationserviceextension) = %{version}

%description
Source code for takopackized Rust crate "objc2-user-notifications"

%package     -n %{name}+nsstring-usernotifications
Summary:        Bindings to the UserNotifications framework - feature "NSString_UserNotifications"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsstring-usernotifications) = %{version}

%description -n %{name}+nsstring-usernotifications
This metapackage enables feature "NSString_UserNotifications" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unerror
Summary:        Bindings to the UserNotifications framework - feature "UNError"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/unerror) = %{version}

%description -n %{name}+unerror
This metapackage enables feature "UNError" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotification
Summary:        Bindings to the UserNotifications framework - feature "UNNotification"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/unnotification) = %{version}

%description -n %{name}+unnotification
This metapackage enables feature "UNNotification" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationaction
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationAction"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/unnotificationaction) = %{version}

%description -n %{name}+unnotificationaction
This metapackage enables feature "UNNotificationAction" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationactionicon
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationActionIcon" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/unnotificationactionicon) = %{version}
Provides:       crate(%{pkgname}/unnotificationrequest) = %{version}
Provides:       crate(%{pkgname}/unnotificationresponse) = %{version}
Provides:       crate(%{pkgname}/unnotificationsound) = %{version}

%description -n %{name}+unnotificationactionicon
This metapackage enables feature "UNNotificationActionIcon" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UNNotificationRequest", "UNNotificationResponse", and "UNNotificationSound" features.

%package     -n %{name}+unnotificationattachment
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationAttachment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/unnotificationattachment) = %{version}

%description -n %{name}+unnotificationattachment
This metapackage enables feature "UNNotificationAttachment" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationcategory
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationCategory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/unnotificationcategory) = %{version}

%description -n %{name}+unnotificationcategory
This metapackage enables feature "UNNotificationCategory" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationcontent
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationContent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/unnotificationcontent) = %{version}

%description -n %{name}+unnotificationcontent
This metapackage enables feature "UNNotificationContent" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationsettings
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationSettings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/unnotificationsettings) = %{version}

%description -n %{name}+unnotificationsettings
This metapackage enables feature "UNNotificationSettings" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationtrigger
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationTrigger"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.2/clregion) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscalendar) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/unnotificationtrigger) = %{version}

%description -n %{name}+unnotificationtrigger
This metapackage enables feature "UNNotificationTrigger" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unusernotificationcenter
Summary:        Bindings to the UserNotifications framework - feature "UNUserNotificationCenter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/unusernotificationcenter) = %{version}

%description -n %{name}+unusernotificationcenter
This metapackage enables feature "UNUserNotificationCenter" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the UserNotifications framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/nsstring-usernotifications) = %{version}
Requires:       crate(%{pkgname}/objc2-core-location) = %{version}
Requires:       crate(%{pkgname}/unerror) = %{version}
Requires:       crate(%{pkgname}/unnotification) = %{version}
Requires:       crate(%{pkgname}/unnotificationaction) = %{version}
Requires:       crate(%{pkgname}/unnotificationactionicon) = %{version}
Requires:       crate(%{pkgname}/unnotificationattachment) = %{version}
Requires:       crate(%{pkgname}/unnotificationcategory) = %{version}
Requires:       crate(%{pkgname}/unnotificationcontent) = %{version}
Requires:       crate(%{pkgname}/unnotificationrequest) = %{version}
Requires:       crate(%{pkgname}/unnotificationresponse) = %{version}
Requires:       crate(%{pkgname}/unnotificationserviceextension) = %{version}
Requires:       crate(%{pkgname}/unnotificationsettings) = %{version}
Requires:       crate(%{pkgname}/unnotificationsound) = %{version}
Requires:       crate(%{pkgname}/unnotificationtrigger) = %{version}
Requires:       crate(%{pkgname}/unusernotificationcenter) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the UserNotifications framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-core-location-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the UserNotifications framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2) >= 2.5.0
Requires:       crate(objc2-foundation-0.2/bitflags) >= 0.2.2
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the UserNotifications framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-core-location-0.2/block2) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-location
Summary:        Bindings to the UserNotifications framework - feature "objc2-core-location"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-core-location) = %{version}

%description -n %{name}+objc2-core-location
This metapackage enables feature "objc2-core-location" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the UserNotifications framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-core-location-0.2/std) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
