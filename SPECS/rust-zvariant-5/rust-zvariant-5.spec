# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zvariant
%global full_version 5.10.1
%global pkgname zvariant-5

Name:           rust-zvariant-5
Version:        5.10.1
Release:        %autorelease
Summary:        Rust crate "zvariant"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:c4db0ecb8987cf5e92653c57c098f7f0e39a03112edb796f4fe089fb7eaa14ff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(endi-1/default) >= 1.1.0
Requires:       crate(serde-1/default) >= 1.0.200
Requires:       crate(serde-1/derive) >= 1.0.200
Requires:       crate(winnow-1/default) >= 1.0.0
Requires:       crate(zvariant-derive-5/default) >= 5.10.1
Requires:       crate(zvariant-utils-3/default) >= 3.3.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/option-as-array) = %{version}

%description
Source code for takopackized Rust crate "zvariant"

%package     -n %{name}+arrayvec
Summary:        D-Bus & GVariant encoding & decoding - feature "arrayvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7/default) >= 0.7.4
Requires:       crate(arrayvec-0.7/serde) >= 0.7.4
Provides:       crate(%{pkgname}/arrayvec) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+camino
Summary:        D-Bus & GVariant encoding & decoding - feature "camino"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(camino-1/default) >= 1.1.9
Provides:       crate(%{pkgname}/camino) = %{version}

%description -n %{name}+camino
This metapackage enables feature "camino" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        D-Bus & GVariant encoding & decoding - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/serde) >= 0.4.38
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+enumflags2
Summary:        D-Bus & GVariant encoding & decoding - feature "enumflags2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(enumflags2-0.7/default) >= 0.7.9
Requires:       crate(enumflags2-0.7/serde) >= 0.7.9
Provides:       crate(%{pkgname}/enumflags2) = %{version}

%description -n %{name}+enumflags2
This metapackage enables feature "enumflags2" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gvariant
Summary:        D-Bus & GVariant encoding & decoding - feature "gvariant" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zvariant-derive-5/gvariant) >= 5.10.1
Requires:       crate(zvariant-utils-3/gvariant) >= 3.3.1
Provides:       crate(%{pkgname}/gvariant) = %{version}
Provides:       crate(%{pkgname}/ostree-tests) = %{version}

%description -n %{name}+gvariant
This metapackage enables feature "gvariant" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ostree-tests" feature.

%package     -n %{name}+heapless
Summary:        D-Bus & GVariant encoding & decoding - feature "heapless"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heapless-0.9/default) >= 0.9.0
Requires:       crate(heapless-0.9/serde) >= 0.9.0
Provides:       crate(%{pkgname}/heapless) = %{version}

%description -n %{name}+heapless
This metapackage enables feature "heapless" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-bytes
Summary:        D-Bus & GVariant encoding & decoding - feature "serde_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-bytes-0.11/default) >= 0.11.14
Provides:       crate(%{pkgname}/serde-bytes) = %{version}

%description -n %{name}+serde-bytes
This metapackage enables feature "serde_bytes" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        D-Bus & GVariant encoding & decoding - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.36
Requires:       crate(time-0.3/serde) >= 0.3.36
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        D-Bus & GVariant encoding & decoding - feature "url"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(url-2/default) >= 2.5.0
Requires:       crate(url-2/serde) >= 2.5.0
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "url" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        D-Bus & GVariant encoding & decoding - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.8.0
Requires:       crate(uuid-1/serde) >= 1.8.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust zvariant crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
