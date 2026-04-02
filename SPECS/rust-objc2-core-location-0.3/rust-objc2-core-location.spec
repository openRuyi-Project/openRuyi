# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-location
%global full_version 0.3.2
%global pkgname objc2-core-location-0.3

Name:           rust-objc2-core-location-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-location"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:ca347214e24bc973fc025fd0d36ebb179ff30536ed1f80252706db19ee452009
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/clavailability)
Provides:       crate(%{pkgname}/clbackgroundactivitysession)
Provides:       crate(%{pkgname}/cllocationmanager-clvisitextensions)
Provides:       crate(%{pkgname}/cllocationupdater)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-location"

%package     -n %{name}+clbeaconidentitycondition
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconIdentityCondition"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/clbeaconidentitycondition)

%description -n %{name}+clbeaconidentitycondition
This metapackage enables feature "CLBeaconIdentityCondition" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clbeaconidentityconstraint
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconIdentityConstraint"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/clbeaconidentityconstraint)

%description -n %{name}+clbeaconidentityconstraint
This metapackage enables feature "CLBeaconIdentityConstraint" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clbeaconregion
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconRegion"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/clbeaconregion)

%description -n %{name}+clbeaconregion
This metapackage enables feature "CLBeaconRegion" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clcirculargeographiccondition
Summary:        Bindings to the CoreLocation framework - feature "CLCircularGeographicCondition" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/clcirculargeographiccondition)
Provides:       crate(%{pkgname}/clcondition)
Provides:       crate(%{pkgname}/clmonitoringrecord)

%description -n %{name}+clcirculargeographiccondition
This metapackage enables feature "CLCircularGeographicCondition" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLCondition", and "CLMonitoringRecord" features.

%package     -n %{name}+clcircularregion
Summary:        Bindings to the CoreLocation framework - feature "CLCircularRegion" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clcircularregion)
Provides:       crate(%{pkgname}/clregion)

%description -n %{name}+clcircularregion
This metapackage enables feature "CLCircularRegion" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLRegion" feature.

%package     -n %{name}+clerror
Summary:        Bindings to the CoreLocation framework - feature "CLError" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clerror)
Provides:       crate(%{pkgname}/clerrordomain)
Provides:       crate(%{pkgname}/clmonitorconfiguration)
Provides:       crate(%{pkgname}/clservicesession)

%description -n %{name}+clerror
This metapackage enables feature "CLError" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLErrorDomain", "CLMonitorConfiguration", and "CLServiceSession" features.

%package     -n %{name}+clgeocoder
Summary:        Bindings to the CoreLocation framework - feature "CLGeocoder"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clgeocoder)

%description -n %{name}+clgeocoder
This metapackage enables feature "CLGeocoder" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clheading
Summary:        Bindings to the CoreLocation framework - feature "CLHeading" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/clheading)
Provides:       crate(%{pkgname}/cllocation)
Provides:       crate(%{pkgname}/clvisit)

%description -n %{name}+clheading
This metapackage enables feature "CLHeading" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLLocation", and "CLVisit" features.

%package     -n %{name}+cllocationmanager
Summary:        Bindings to the CoreLocation framework - feature "CLLocationManager"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationmanager)

%description -n %{name}+cllocationmanager
This metapackage enables feature "CLLocationManager" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationmanagerdelegate
Summary:        Bindings to the CoreLocation framework - feature "CLLocationManagerDelegate"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationmanagerdelegate)

%description -n %{name}+cllocationmanagerdelegate
This metapackage enables feature "CLLocationManagerDelegate" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationpushserviceerror
Summary:        Bindings to the CoreLocation framework - feature "CLLocationPushServiceError"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationpushserviceerror)

%description -n %{name}+cllocationpushserviceerror
This metapackage enables feature "CLLocationPushServiceError" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationpushserviceextension
Summary:        Bindings to the CoreLocation framework - feature "CLLocationPushServiceExtension"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationpushserviceextension)

%description -n %{name}+cllocationpushserviceextension
This metapackage enables feature "CLLocationPushServiceExtension" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clmonitor
Summary:        Bindings to the CoreLocation framework - feature "CLMonitor"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clmonitor)

%description -n %{name}+clmonitor
This metapackage enables feature "CLMonitor" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clmonitoringevent
Summary:        Bindings to the CoreLocation framework - feature "CLMonitoringEvent"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clmonitoringevent)

%description -n %{name}+clmonitoringevent
This metapackage enables feature "CLMonitoringEvent" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clplacemark
Summary:        Bindings to the CoreLocation framework - feature "CLPlacemark"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/clplacemark)

%description -n %{name}+clplacemark
This metapackage enables feature "CLPlacemark" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreLocation framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreLocation framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/clavailability)
Requires:       crate(%{pkgname}/clbackgroundactivitysession)
Requires:       crate(%{pkgname}/clbeaconidentitycondition)
Requires:       crate(%{pkgname}/clbeaconidentityconstraint)
Requires:       crate(%{pkgname}/clbeaconregion)
Requires:       crate(%{pkgname}/clcirculargeographiccondition)
Requires:       crate(%{pkgname}/clcircularregion)
Requires:       crate(%{pkgname}/clcondition)
Requires:       crate(%{pkgname}/clerror)
Requires:       crate(%{pkgname}/clerrordomain)
Requires:       crate(%{pkgname}/clgeocoder)
Requires:       crate(%{pkgname}/clheading)
Requires:       crate(%{pkgname}/cllocation)
Requires:       crate(%{pkgname}/cllocationmanager)
Requires:       crate(%{pkgname}/cllocationmanager-clvisitextensions)
Requires:       crate(%{pkgname}/cllocationmanagerdelegate)
Requires:       crate(%{pkgname}/cllocationpushserviceerror)
Requires:       crate(%{pkgname}/cllocationpushserviceextension)
Requires:       crate(%{pkgname}/cllocationupdater)
Requires:       crate(%{pkgname}/clmonitor)
Requires:       crate(%{pkgname}/clmonitorconfiguration)
Requires:       crate(%{pkgname}/clmonitoringevent)
Requires:       crate(%{pkgname}/clmonitoringrecord)
Requires:       crate(%{pkgname}/clplacemark)
Requires:       crate(%{pkgname}/clregion)
Requires:       crate(%{pkgname}/clservicesession)
Requires:       crate(%{pkgname}/clvisit)
Requires:       crate(%{pkgname}/dispatch2)
Requires:       crate(%{pkgname}/objc2-contacts)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the CoreLocation framework - feature "dispatch2"
Requires:       crate(%{pkgname})
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.0
Provides:       crate(%{pkgname}/dispatch2)

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-contacts
Summary:        Bindings to the CoreLocation framework - feature "objc2-contacts"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-contacts-0.3/cnpostaladdress) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-contacts)

%description -n %{name}+objc2-contacts
This metapackage enables feature "objc2-contacts" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
