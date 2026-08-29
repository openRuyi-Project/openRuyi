# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-user-notifications
%global full_version 0.3.2
%global pkgname objc2-user-notifications-0.3

Name:           rust-objc2-user-notifications-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-user-notifications"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:9df9128cbbfef73cda168416ccf7f837b62737d748333bfe9ab71c245d76613e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unnotificationattributedmessagecontext) = %{version}
Provides:       crate(%{pkgname}/unnotificationserviceextension) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-user-notifications"

%package     -n %{name}+nsstring-usernotifications
Summary:        Bindings to the UserNotifications framework - feature "NSString_UserNotifications"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsstring-usernotifications) = %{version}

%description -n %{name}+nsstring-usernotifications
This metapackage enables feature "NSString_UserNotifications" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unerror
Summary:        Bindings to the UserNotifications framework - feature "UNError"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unerror) = %{version}

%description -n %{name}+unerror
This metapackage enables feature "UNError" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotification
Summary:        Bindings to the UserNotifications framework - feature "UNNotification"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/unnotification) = %{version}

%description -n %{name}+unnotification
This metapackage enables feature "UNNotification" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationaction
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationAction"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationaction) = %{version}

%description -n %{name}+unnotificationaction
This metapackage enables feature "UNNotificationAction" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationactionicon
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationActionIcon" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
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
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationattachment) = %{version}

%description -n %{name}+unnotificationattachment
This metapackage enables feature "UNNotificationAttachment" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationcategory
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationCategory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationcategory) = %{version}

%description -n %{name}+unnotificationcategory
This metapackage enables feature "UNNotificationCategory" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationcontent
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationContent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationcontent) = %{version}

%description -n %{name}+unnotificationcontent
This metapackage enables feature "UNNotificationContent" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationsettings
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationSettings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationsettings) = %{version}

%description -n %{name}+unnotificationsettings
This metapackage enables feature "UNNotificationSettings" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationtrigger
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationTrigger"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationtrigger) = %{version}

%description -n %{name}+unnotificationtrigger
This metapackage enables feature "UNNotificationTrigger" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unusernotificationcenter
Summary:        Bindings to the UserNotifications framework - feature "UNUserNotificationCenter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unusernotificationcenter) = %{version}

%description -n %{name}+unusernotificationcenter
This metapackage enables feature "UNUserNotificationCenter" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the UserNotifications framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the UserNotifications framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the UserNotifications framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/nsstring-usernotifications) = %{version}
Requires:       crate(%{pkgname}/objc2-core-location) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unerror) = %{version}
Requires:       crate(%{pkgname}/unnotification) = %{version}
Requires:       crate(%{pkgname}/unnotificationaction) = %{version}
Requires:       crate(%{pkgname}/unnotificationactionicon) = %{version}
Requires:       crate(%{pkgname}/unnotificationattachment) = %{version}
Requires:       crate(%{pkgname}/unnotificationattributedmessagecontext) = %{version}
Requires:       crate(%{pkgname}/unnotificationcategory) = %{version}
Requires:       crate(%{pkgname}/unnotificationcontent) = %{version}
Requires:       crate(%{pkgname}/unnotificationrequest) = %{version}
Requires:       crate(%{pkgname}/unnotificationresponse) = %{version}
Requires:       crate(%{pkgname}/unnotificationserviceextension) = %{version}
Requires:       crate(%{pkgname}/unnotificationsettings) = %{version}
Requires:       crate(%{pkgname}/unnotificationsound) = %{version}
Requires:       crate(%{pkgname}/unnotificationtrigger) = %{version}
Requires:       crate(%{pkgname}/unusernotificationcenter) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-location
Summary:        Bindings to the UserNotifications framework - feature "objc2-core-location"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.3/clregion) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-location) = %{version}

%description -n %{name}+objc2-core-location
This metapackage enables feature "objc2-core-location" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
