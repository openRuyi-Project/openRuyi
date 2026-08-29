# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atspi-common
%global full_version 0.9.0
%global pkgname atspi-common-0.9

Name:           rust-atspi-common-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "atspi-common"
License:        Apache-2.0 OR MIT
URL:            https://github.com/odilia-app/atspi
#!RemoteAsset:  sha256:33dfc05e7cdf90988a197803bf24f5788f94f7c94a69efa95683e8ffe76cfdfb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(enumflags2-0.7/default) >= 0.7.7
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(static-assertions-1/default) >= 1.1.0
Requires:       crate(zbus-lockstep-0.5/default) >= 0.5.0
Requires:       crate(zbus-lockstep-macros-0.5/default) >= 0.5.0
Requires:       crate(zbus-names-4/default) >= 4.0.0
Requires:       crate(zvariant-5) >= 5.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/wrappers) = %{version}

%description
Source code for takopackized Rust crate "atspi-common"

%package     -n %{name}+async-std
Summary:        Primitive types used for sending and receiving Linux accessibility events - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zbus-5/async-io) >= 5.5.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust atspi-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Primitive types used for sending and receiving Linux accessibility events - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Requires:       crate(%{pkgname}/wrappers) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust atspi-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Primitive types used for sending and receiving Linux accessibility events - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zbus-5/tokio) >= 5.5.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust atspi-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zbus
Summary:        Primitive types used for sending and receiving Linux accessibility events - feature "zbus"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zbus-5) >= 5.5.0
Provides:       crate(%{pkgname}/zbus) = %{version}

%description -n %{name}+zbus
This metapackage enables feature "zbus" for the Rust atspi-common crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
