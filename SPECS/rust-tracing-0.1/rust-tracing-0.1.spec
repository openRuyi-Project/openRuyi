# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing
%global full_version 0.1.44
%global pkgname tracing-0.1

Name:           rust-tracing-0.1
Version:        0.1.44
Release:        %autorelease
Summary:        Rust crate "tracing"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:63e71662fa4b2a2c3a26f570f037eb95bb1f85397f3cd8076caed2f026a6d100
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-lite-0.2/default) >= 0.2.9
Requires:       crate(tracing-core-0.1) >= 0.1.36
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async-await) = %{version}
Provides:       crate(%{pkgname}/max-level-debug) = %{version}
Provides:       crate(%{pkgname}/max-level-error) = %{version}
Provides:       crate(%{pkgname}/max-level-info) = %{version}
Provides:       crate(%{pkgname}/max-level-off) = %{version}
Provides:       crate(%{pkgname}/max-level-trace) = %{version}
Provides:       crate(%{pkgname}/max-level-warn) = %{version}
Provides:       crate(%{pkgname}/release-max-level-debug) = %{version}
Provides:       crate(%{pkgname}/release-max-level-error) = %{version}
Provides:       crate(%{pkgname}/release-max-level-info) = %{version}
Provides:       crate(%{pkgname}/release-max-level-off) = %{version}
Provides:       crate(%{pkgname}/release-max-level-trace) = %{version}
Provides:       crate(%{pkgname}/release-max-level-warn) = %{version}

%description
Source code for takopackized Rust crate "tracing"

%package     -n %{name}+default
Summary:        Application-level tracing for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracing crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Application-level tracing for Rust - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.17
Provides:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/log-always) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust tracing crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "log-always" feature.

%package     -n %{name}+std
Summary:        Application-level tracing for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-core-0.1/std) >= 0.1.36
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tracing crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-attributes
Summary:        Application-level tracing for Rust - feature "tracing-attributes" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-attributes-0.1/default) >= 0.1.31
Provides:       crate(%{pkgname}/attributes) = %{version}
Provides:       crate(%{pkgname}/tracing-attributes) = %{version}

%description -n %{name}+tracing-attributes
This metapackage enables feature "tracing-attributes" for the Rust tracing crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "attributes" feature.

%package     -n %{name}+valuable
Summary:        Application-level tracing for Rust - feature "valuable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-core-0.1/valuable) >= 0.1.36
Provides:       crate(%{pkgname}/valuable) = %{version}

%description -n %{name}+valuable
This metapackage enables feature "valuable" for the Rust tracing crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
