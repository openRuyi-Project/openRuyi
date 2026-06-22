# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-location
%global full_version 0.2.2
%global pkgname objc2-core-location-0.2

Name:           rust-objc2-core-location-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-location"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:000cfee34e683244f284252ee206a27953279d370e309649dc3ee317b37e5781
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clavailability) = %{version}
Provides:       crate(%{pkgname}/clbackgroundactivitysession) = %{version}
Provides:       crate(%{pkgname}/cllocationmanager-clvisitextensions) = %{version}
Provides:       crate(%{pkgname}/cllocationupdater) = %{version}

%description
Source code for takopackized Rust crate "objc2-core-location"

%package     -n %{name}+clbeaconidentitycondition
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconIdentityCondition"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuuid) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/clbeaconidentitycondition) = %{version}

%description -n %{name}+clbeaconidentitycondition
This metapackage enables feature "CLBeaconIdentityCondition" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clbeaconidentityconstraint
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconIdentityConstraint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuuid) >= 0.2.2
Provides:       crate(%{pkgname}/clbeaconidentityconstraint) = %{version}

%description -n %{name}+clbeaconidentityconstraint
This metapackage enables feature "CLBeaconIdentityConstraint" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clbeaconregion
Summary:        Bindings to the CoreLocation framework - feature "CLBeaconRegion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuuid) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/clbeaconregion) = %{version}

%description -n %{name}+clbeaconregion
This metapackage enables feature "CLBeaconRegion" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clcirculargeographiccondition
Summary:        Bindings to the CoreLocation framework - feature "CLCircularGeographicCondition" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/clcirculargeographiccondition) = %{version}
Provides:       crate(%{pkgname}/clcondition) = %{version}
Provides:       crate(%{pkgname}/clmonitoringrecord) = %{version}

%description -n %{name}+clcirculargeographiccondition
This metapackage enables feature "CLCircularGeographicCondition" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLCondition", and "CLMonitoringRecord" features.

%package     -n %{name}+clcircularregion
Summary:        Bindings to the CoreLocation framework - feature "CLCircularRegion" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/clcircularregion) = %{version}
Provides:       crate(%{pkgname}/clregion) = %{version}

%description -n %{name}+clcircularregion
This metapackage enables feature "CLCircularRegion" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLRegion" feature.

%package     -n %{name}+clerror
Summary:        Bindings to the CoreLocation framework - feature "CLError" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/clerror) = %{version}
Provides:       crate(%{pkgname}/clerrordomain) = %{version}
Provides:       crate(%{pkgname}/clmonitorconfiguration) = %{version}

%description -n %{name}+clerror
This metapackage enables feature "CLError" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLErrorDomain", and "CLMonitorConfiguration" features.

%package     -n %{name}+clgeocoder
Summary:        Bindings to the CoreLocation framework - feature "CLGeocoder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-contacts-0.2/cnpostaladdress) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslocale) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/clgeocoder) = %{version}

%description -n %{name}+clgeocoder
This metapackage enables feature "CLGeocoder" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clheading
Summary:        Bindings to the CoreLocation framework - feature "CLHeading" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/clheading) = %{version}
Provides:       crate(%{pkgname}/cllocation) = %{version}
Provides:       crate(%{pkgname}/clvisit) = %{version}

%description -n %{name}+clheading
This metapackage enables feature "CLHeading" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CLLocation", and "CLVisit" features.

%package     -n %{name}+cllocationmanager
Summary:        Bindings to the CoreLocation framework - feature "CLLocationManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cllocationmanager) = %{version}

%description -n %{name}+cllocationmanager
This metapackage enables feature "CLLocationManager" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationmanagerdelegate
Summary:        Bindings to the CoreLocation framework - feature "CLLocationManagerDelegate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Provides:       crate(%{pkgname}/cllocationmanagerdelegate) = %{version}

%description -n %{name}+cllocationmanagerdelegate
This metapackage enables feature "CLLocationManagerDelegate" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationpushserviceerror
Summary:        Bindings to the CoreLocation framework - feature "CLLocationPushServiceError"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cllocationpushserviceerror) = %{version}

%description -n %{name}+cllocationpushserviceerror
This metapackage enables feature "CLLocationPushServiceError" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cllocationpushserviceextension
Summary:        Bindings to the CoreLocation framework - feature "CLLocationPushServiceExtension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cllocationpushserviceextension) = %{version}

%description -n %{name}+cllocationpushserviceextension
This metapackage enables feature "CLLocationPushServiceExtension" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clmonitor
Summary:        Bindings to the CoreLocation framework - feature "CLMonitor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/clmonitor) = %{version}

%description -n %{name}+clmonitor
This metapackage enables feature "CLMonitor" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clmonitoringevent
Summary:        Bindings to the CoreLocation framework - feature "CLMonitoringEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/clmonitoringevent) = %{version}

%description -n %{name}+clmonitoringevent
This metapackage enables feature "CLMonitoringEvent" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clplacemark
Summary:        Bindings to the CoreLocation framework - feature "CLPlacemark"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-contacts-0.2/cnpostaladdress) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nstimezone) >= 0.2.2
Provides:       crate(%{pkgname}/clplacemark) = %{version}

%description -n %{name}+clplacemark
This metapackage enables feature "CLPlacemark" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the CoreLocation framework - feature "all"
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
Requires:       crate(%{pkgname}/clvisit) = %{version}
Requires:       crate(%{pkgname}/objc2-contacts) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the CoreLocation framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-contacts-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreLocation framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-contacts-0.2/block2) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-contacts
Summary:        Bindings to the CoreLocation framework - feature "objc2-contacts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-contacts-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-contacts) = %{version}

%description -n %{name}+objc2-contacts
This metapackage enables feature "objc2-contacts" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the CoreLocation framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-contacts-0.2/std) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-core-location crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
