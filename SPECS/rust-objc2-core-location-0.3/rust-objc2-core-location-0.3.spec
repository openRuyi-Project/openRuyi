# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/clavailability) = %{version}
Provides:       crate(%{pkgname}/clbackgroundactivitysession) = %{version}
Provides:       crate(%{pkgname}/cllocationmanager-clvisitextensions) = %{version}
Provides:       crate(%{pkgname}/cllocationupdater) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-core-location"

%package     -n %{name}+clbeaconidentitycondition
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconIdentityCondition"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/clbeaconidentitycondition) = %{version}

%description -n %{name}+clbeaconidentitycondition
This metapackage enables feature "CLBeaconIdentityCondition" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clbeaconidentityconstraint
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconIdentityConstraint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/clbeaconidentityconstraint) = %{version}

%description -n %{name}+clbeaconidentityconstraint
This metapackage enables feature "CLBeaconIdentityConstraint" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clbeaconregion
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconRegion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/clbeaconregion) = %{version}

%description -n %{name}+clbeaconregion
This metapackage enables feature "CLBeaconRegion" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clcirculargeographiccondition
Summary:        Bindings to the CoreLocation framework - feature "CLCircularGeographicCondition" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/clcirculargeographiccondition) = %{version}
Provides:       crate(%{pkgname}/clcondition) = %{version}
Provides:       crate(%{pkgname}/clmonitoringrecord) = %{version}

%description -n %{name}+clcirculargeographiccondition
This metapackage enables feature "CLCircularGeographicCondition" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLCondition", and "CLMonitoringRecord" features.

%package     -n %{name}+clcircularregion
Summary:        Bindings to the CoreLocation framework - feature "CLCircularRegion" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clcircularregion) = %{version}
Provides:       crate(%{pkgname}/clregion) = %{version}

%description -n %{name}+clcircularregion
This metapackage enables feature "CLCircularRegion" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLRegion" feature.

%package     -n %{name}+clerror
Summary:        Bindings to the CoreLocation framework - feature "CLError" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clerror) = %{version}
Provides:       crate(%{pkgname}/clerrordomain) = %{version}
Provides:       crate(%{pkgname}/clmonitorconfiguration) = %{version}
Provides:       crate(%{pkgname}/clservicesession) = %{version}

%description -n %{name}+clerror
This metapackage enables feature "CLError" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLErrorDomain", "CLMonitorConfiguration", and "CLServiceSession" features.

%package     -n %{name}+clgeocoder
Summary:        Bindings to the CoreLocation framework - feature "CLGeocoder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clgeocoder) = %{version}

%description -n %{name}+clgeocoder
This metapackage enables feature "CLGeocoder" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clheading
Summary:        Bindings to the CoreLocation framework - feature "CLHeading" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/clheading) = %{version}
Provides:       crate(%{pkgname}/cllocation) = %{version}
Provides:       crate(%{pkgname}/clvisit) = %{version}

%description -n %{name}+clheading
This metapackage enables feature "CLHeading" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLLocation", and "CLVisit" features.

%package     -n %{name}+cllocationmanager
Summary:        Bindings to the CoreLocation framework - feature "CLLocationManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationmanager) = %{version}

%description -n %{name}+cllocationmanager
This metapackage enables feature "CLLocationManager" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationmanagerdelegate
Summary:        Bindings to the CoreLocation framework - feature "CLLocationManagerDelegate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationmanagerdelegate) = %{version}

%description -n %{name}+cllocationmanagerdelegate
This metapackage enables feature "CLLocationManagerDelegate" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationpushserviceerror
Summary:        Bindings to the CoreLocation framework - feature "CLLocationPushServiceError"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationpushserviceerror) = %{version}

%description -n %{name}+cllocationpushserviceerror
This metapackage enables feature "CLLocationPushServiceError" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationpushserviceextension
Summary:        Bindings to the CoreLocation framework - feature "CLLocationPushServiceExtension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cllocationpushserviceextension) = %{version}

%description -n %{name}+cllocationpushserviceextension
This metapackage enables feature "CLLocationPushServiceExtension" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clmonitor
Summary:        Bindings to the CoreLocation framework - feature "CLMonitor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clmonitor) = %{version}

%description -n %{name}+clmonitor
This metapackage enables feature "CLMonitor" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clmonitoringevent
Summary:        Bindings to the CoreLocation framework - feature "CLMonitoringEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/clmonitoringevent) = %{version}

%description -n %{name}+clmonitoringevent
This metapackage enables feature "CLMonitoringEvent" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clplacemark
Summary:        Bindings to the CoreLocation framework - feature "CLPlacemark"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/clplacemark) = %{version}

%description -n %{name}+clplacemark
This metapackage enables feature "CLPlacemark" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreLocation framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreLocation framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/clavailability) = %{version}
Requires:       crate(%{pkgname}/clbackgroundactivitysession) = %{version}
Requires:       crate(%{pkgname}/clbeaconidentitycondition) = %{version}
Requires:       crate(%{pkgname}/clbeaconidentityconstraint) = %{version}
Requires:       crate(%{pkgname}/clbeaconregion) = %{version}
Requires:       crate(%{pkgname}/clcirculargeographiccondition) = %{version}
Requires:       crate(%{pkgname}/clcircularregion) = %{version}
Requires:       crate(%{pkgname}/clcondition) = %{version}
Requires:       crate(%{pkgname}/clerror) = %{version}
Requires:       crate(%{pkgname}/clerrordomain) = %{version}
Requires:       crate(%{pkgname}/clgeocoder) = %{version}
Requires:       crate(%{pkgname}/clheading) = %{version}
Requires:       crate(%{pkgname}/cllocation) = %{version}
Requires:       crate(%{pkgname}/cllocationmanager) = %{version}
Requires:       crate(%{pkgname}/cllocationmanager-clvisitextensions) = %{version}
Requires:       crate(%{pkgname}/cllocationmanagerdelegate) = %{version}
Requires:       crate(%{pkgname}/cllocationpushserviceerror) = %{version}
Requires:       crate(%{pkgname}/cllocationpushserviceextension) = %{version}
Requires:       crate(%{pkgname}/cllocationupdater) = %{version}
Requires:       crate(%{pkgname}/clmonitor) = %{version}
Requires:       crate(%{pkgname}/clmonitorconfiguration) = %{version}
Requires:       crate(%{pkgname}/clmonitoringevent) = %{version}
Requires:       crate(%{pkgname}/clmonitoringrecord) = %{version}
Requires:       crate(%{pkgname}/clplacemark) = %{version}
Requires:       crate(%{pkgname}/clregion) = %{version}
Requires:       crate(%{pkgname}/clservicesession) = %{version}
Requires:       crate(%{pkgname}/clvisit) = %{version}
Requires:       crate(%{pkgname}/dispatch2) = %{version}
Requires:       crate(%{pkgname}/objc2-contacts) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the CoreLocation framework - feature "dispatch2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.0
Provides:       crate(%{pkgname}/dispatch2) = %{version}

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-contacts
Summary:        Bindings to the CoreLocation framework - feature "objc2-contacts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-contacts-0.3/cnpostaladdress) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-contacts) = %{version}

%description -n %{name}+objc2-contacts
This metapackage enables feature "objc2-contacts" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
