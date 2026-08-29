# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gbm-sys
%global full_version 0.4.0
%global pkgname gbm-sys-0.4

Name:           rust-gbm-sys-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "gbm-sys"
License:        MIT
URL:            https://github.com/Drakulix/gbm.rs/tree/master/gbm-sys
#!RemoteAsset:  sha256:c13a5f2acc785d8fb6bf6b7ab6bfb0ef5dad4f4d97e8e70bb8e470722312f76f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gbm-sys"

%package     -n %{name}+bindgen
Summary:        Bindgen generated unsafe libgbm wrapper - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.69/default) >= 0.69.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust gbm-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-bindgen
Summary:        Bindgen generated unsafe libgbm wrapper - feature "use_bindgen" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Requires:       crate(proc-macro2-1/default) >= 1.0.69
Requires:       crate(regex-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/update-bindings) = %{version}
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust gbm-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "update_bindings" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
