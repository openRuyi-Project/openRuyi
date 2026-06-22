# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name input
%global full_version 0.9.1
%global pkgname input-0.9

Name:           rust-input-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "input"
License:        MIT
URL:            https://github.com/Drakulix/input.rs
#!RemoteAsset:  sha256:fbdc09524a91f9cacd26f16734ff63d7dc650daffadd2b6f84d17a285bd875a9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(input-sys-1) >= 1.18.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "input"

%package     -n %{name}+default
Summary:        Libinput bindings for rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libinput-1-21) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/udev) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libinput-1-11
Summary:        Libinput bindings for rust - feature "libinput_1_11"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(input-sys-1/libinput-1-11) >= 1.18.0
Provides:       crate(%{pkgname}/libinput-1-11) = %{version}

%description -n %{name}+libinput-1-11
This metapackage enables feature "libinput_1_11" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libinput-1-14
Summary:        Libinput bindings for rust - feature "libinput_1_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libinput-1-11) = %{version}
Requires:       crate(input-sys-1/libinput-1-14) >= 1.18.0
Provides:       crate(%{pkgname}/libinput-1-14) = %{version}

%description -n %{name}+libinput-1-14
This metapackage enables feature "libinput_1_14" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libinput-1-15
Summary:        Libinput bindings for rust - feature "libinput_1_15"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libinput-1-14) = %{version}
Requires:       crate(input-sys-1/libinput-1-15) >= 1.18.0
Provides:       crate(%{pkgname}/libinput-1-15) = %{version}

%description -n %{name}+libinput-1-15
This metapackage enables feature "libinput_1_15" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libinput-1-19
Summary:        Libinput bindings for rust - feature "libinput_1_19"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libinput-1-15) = %{version}
Requires:       crate(input-sys-1/libinput-1-19) >= 1.18.0
Provides:       crate(%{pkgname}/libinput-1-19) = %{version}

%description -n %{name}+libinput-1-19
This metapackage enables feature "libinput_1_19" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libinput-1-21
Summary:        Libinput bindings for rust - feature "libinput_1_21"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libinput-1-19) = %{version}
Requires:       crate(input-sys-1/libinput-1-21) >= 1.18.0
Provides:       crate(%{pkgname}/libinput-1-21) = %{version}

%description -n %{name}+libinput-1-21
This metapackage enables feature "libinput_1_21" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Libinput bindings for rust - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.20
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+udev
Summary:        Libinput bindings for rust - feature "udev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(udev-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/udev) = %{version}

%description -n %{name}+udev
This metapackage enables feature "udev" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-bindgen
Summary:        Libinput bindings for rust - feature "use_bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(input-sys-1/use-bindgen) >= 1.18.0
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+use-bindgen
This metapackage enables feature "use_bindgen" for the Rust input crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
