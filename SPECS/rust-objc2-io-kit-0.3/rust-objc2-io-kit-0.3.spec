# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-io-kit
%global full_version 0.3.2
%global pkgname objc2-io-kit-0.3

Name:           rust-objc2-io-kit-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-io-kit"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:33fafba39597d6dc1fb709123dfa8289d39406734be322956a69f0931c73bb15
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/appleusbdefinitions) = %{version}
Provides:       crate(%{pkgname}/iousbhostfamilydefinitions) = %{version}
Provides:       crate(%{pkgname}/network) = %{version}
Provides:       crate(%{pkgname}/serial) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}
Provides:       crate(%{pkgname}/usb) = %{version}
Provides:       crate(%{pkgname}/usbspec) = %{version}

%description
Source code for takopackized Rust crate "objc2-io-kit"

%package     -n %{name}+iousblib
Summary:        Bindings to the IOKit framework - feature "IOUSBLib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Provides:       crate(%{pkgname}/iousblib) = %{version}

%description -n %{name}+iousblib
This metapackage enables feature "IOUSBLib" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the IOKit framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the IOKit framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the IOKit framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/appleusbdefinitions) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/dispatch2) = %{version}
Requires:       crate(%{pkgname}/graphics) = %{version}
Requires:       crate(%{pkgname}/hid) = %{version}
Requires:       crate(%{pkgname}/hidsystem) = %{version}
Requires:       crate(%{pkgname}/iousbhostfamilydefinitions) = %{version}
Requires:       crate(%{pkgname}/iousblib) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/network) = %{version}
Requires:       crate(%{pkgname}/objc2) = %{version}
Requires:       crate(%{pkgname}/ps) = %{version}
Requires:       crate(%{pkgname}/pwr-mgt) = %{version}
Requires:       crate(%{pkgname}/serial) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/usb) = %{version}
Requires:       crate(%{pkgname}/usbspec) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the IOKit framework - feature "dispatch2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Requires:       crate(dispatch2-0.3/block2) >= 0.3.0
Provides:       crate(%{pkgname}/dispatch2) = %{version}

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+graphics
Summary:        Bindings to the IOKit framework - feature "graphics"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Provides:       crate(%{pkgname}/graphics) = %{version}

%description -n %{name}+graphics
This metapackage enables feature "graphics" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hid
Summary:        Bindings to the IOKit framework - feature "hid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfset) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Provides:       crate(%{pkgname}/hid) = %{version}

%description -n %{name}+hid
This metapackage enables feature "hid" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hidsystem
Summary:        Bindings to the IOKit framework - feature "hidsystem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Provides:       crate(%{pkgname}/hidsystem) = %{version}

%description -n %{name}+hidsystem
This metapackage enables feature "hidsystem" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the IOKit framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the IOKit framework - feature "objc2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Requires:       crate(dispatch2-0.3/block2) >= 0.3.0
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.0
Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2) = %{version}

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ps
Summary:        Bindings to the IOKit framework - feature "ps"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfset) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Provides:       crate(%{pkgname}/ps) = %{version}

%description -n %{name}+ps
This metapackage enables feature "ps" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pwr-mgt
Summary:        Bindings to the IOKit framework - feature "pwr_mgt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfplugincom) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfuuid) >= 0.3.2
Provides:       crate(%{pkgname}/pwr-mgt) = %{version}

%description -n %{name}+pwr-mgt
This metapackage enables feature "pwr_mgt" for the Rust objc2-io-kit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
