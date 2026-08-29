# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name input-sys
%global full_version 1.19.0
%global pkgname input-sys-1

Name:           rust-input-sys-1
Version:        1.19.0
Release:        %autorelease
Summary:        Rust crate "input-sys"
License:        MIT
URL:            https://github.com/Drakulix/input.rs/tree/master/input-sys
#!RemoteAsset:  sha256:36eee07d8e02bd95bf52b2e642cf13d33701b94c6e4b04fbf1d1fb07e9cb19e7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/libinput-1-11) = %{version}
Provides:       crate(%{pkgname}/libinput-1-14) = %{version}
Provides:       crate(%{pkgname}/libinput-1-15) = %{version}
Provides:       crate(%{pkgname}/libinput-1-19) = %{version}
Provides:       crate(%{pkgname}/libinput-1-21) = %{version}
Provides:       crate(%{pkgname}/libinput-1-23) = %{version}
Provides:       crate(%{pkgname}/libinput-1-26) = %{version}
Provides:       crate(%{pkgname}/libinput-1-27) = %{version}
Provides:       crate(%{pkgname}/libinput-1-28) = %{version}
Provides:       crate(%{pkgname}/libinput-1-29) = %{version}
Provides:       crate(%{pkgname}/libinput-1-30) = %{version}

%description
Source code for takopackized Rust crate "input-sys"

%package     -n %{name}+bindgen
Summary:        Bindgen generated unsafe libinput wrapper - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.72/default) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust input-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro2
Summary:        Bindgen generated unsafe libinput wrapper - feature "proc-macro2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/default) >= 1.0.76
Provides:       crate(%{pkgname}/proc-macro2) = %{version}

%description -n %{name}+proc-macro2
This metapackage enables feature "proc-macro2" for the Rust input-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Bindgen generated unsafe libinput wrapper - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust input-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-bindgen
Summary:        Bindgen generated unsafe libinput wrapper - feature "use_bindgen" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Requires:       crate(%{pkgname}/proc-macro2) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Provides:       crate(%{pkgname}/update-bindings) = %{version}
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust input-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "update_bindings" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
