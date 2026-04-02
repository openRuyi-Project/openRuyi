# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unnotificationattributedmessagecontext)
Provides:       crate(%{pkgname}/unnotificationserviceextension)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-user-notifications"

%package     -n %{name}+nsstring-usernotifications
Summary:        Bindings to the UserNotifications framework - feature "NSString_UserNotifications"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsstring-usernotifications)

%description -n %{name}+nsstring-usernotifications
This metapackage enables feature "NSString_UserNotifications" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unerror
Summary:        Bindings to the UserNotifications framework - feature "UNError"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unerror)

%description -n %{name}+unerror
This metapackage enables feature "UNError" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotification
Summary:        Bindings to the UserNotifications framework - feature "UNNotification"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/unnotification)

%description -n %{name}+unnotification
This metapackage enables feature "UNNotification" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationaction
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationAction"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationaction)

%description -n %{name}+unnotificationaction
This metapackage enables feature "UNNotificationAction" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationactionicon
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationActionIcon" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationactionicon)
Provides:       crate(%{pkgname}/unnotificationrequest)
Provides:       crate(%{pkgname}/unnotificationresponse)
Provides:       crate(%{pkgname}/unnotificationsound)

%description -n %{name}+unnotificationactionicon
This metapackage enables feature "UNNotificationActionIcon" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UNNotificationRequest", "UNNotificationResponse", and "UNNotificationSound" features.

%package     -n %{name}+unnotificationattachment
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationAttachment"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationattachment)

%description -n %{name}+unnotificationattachment
This metapackage enables feature "UNNotificationAttachment" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationcategory
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationCategory"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationcategory)

%description -n %{name}+unnotificationcategory
This metapackage enables feature "UNNotificationCategory" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationcontent
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationContent"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationcontent)

%description -n %{name}+unnotificationcontent
This metapackage enables feature "UNNotificationContent" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationsettings
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationSettings"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationsettings)

%description -n %{name}+unnotificationsettings
This metapackage enables feature "UNNotificationSettings" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unnotificationtrigger
Summary:        Bindings to the UserNotifications framework - feature "UNNotificationTrigger"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/unnotificationtrigger)

%description -n %{name}+unnotificationtrigger
This metapackage enables feature "UNNotificationTrigger" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unusernotificationcenter
Summary:        Bindings to the UserNotifications framework - feature "UNUserNotificationCenter"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/unusernotificationcenter)

%description -n %{name}+unusernotificationcenter
This metapackage enables feature "UNUserNotificationCenter" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the UserNotifications framework - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the UserNotifications framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the UserNotifications framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/nsstring-usernotifications)
Requires:       crate(%{pkgname}/objc2-core-location)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unerror)
Requires:       crate(%{pkgname}/unnotification)
Requires:       crate(%{pkgname}/unnotificationaction)
Requires:       crate(%{pkgname}/unnotificationactionicon)
Requires:       crate(%{pkgname}/unnotificationattachment)
Requires:       crate(%{pkgname}/unnotificationattributedmessagecontext)
Requires:       crate(%{pkgname}/unnotificationcategory)
Requires:       crate(%{pkgname}/unnotificationcontent)
Requires:       crate(%{pkgname}/unnotificationrequest)
Requires:       crate(%{pkgname}/unnotificationresponse)
Requires:       crate(%{pkgname}/unnotificationserviceextension)
Requires:       crate(%{pkgname}/unnotificationsettings)
Requires:       crate(%{pkgname}/unnotificationsound)
Requires:       crate(%{pkgname}/unnotificationtrigger)
Requires:       crate(%{pkgname}/unusernotificationcenter)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-location
Summary:        Bindings to the UserNotifications framework - feature "objc2-core-location"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-location-0.3/clregion) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-location)

%description -n %{name}+objc2-core-location
This metapackage enables feature "objc2-core-location" for the Rust objc2-user-notifications crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
