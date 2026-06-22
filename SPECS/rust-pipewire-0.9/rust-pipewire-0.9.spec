# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pipewire
%global full_version 0.9.2
%global pkgname pipewire-0.9

Name:           rust-pipewire-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "pipewire"
License:        MIT
URL:            https://pipewire.org
#!RemoteAsset:  sha256:9688b89abf11d756499f7c6190711d6dbe5a3acdb30c8fbf001d6596d06a8d44
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libspa-0.9/default) >= 0.9.0
Requires:       crate(libspa-sys-0.9/default) >= 0.9.0
Requires:       crate(nix-0.30/default) >= 0.30.1
Requires:       crate(nix-0.30/fs) >= 0.30.1
Requires:       crate(nix-0.30/signal) >= 0.30.1
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(pipewire-sys-0.9/default) >= 0.9.0
Requires:       crate(thiserror-2/default) >= 2.0.12
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v0-3-32) = %{version}

%description
Source code for takopackized Rust crate "pipewire"

%package     -n %{name}+v0-3-33
Summary:        Rust bindings for PipeWire - feature "v0_3_33" and 11 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v0-3-32) = %{version}
Requires:       crate(libspa-0.9/v0-3-33) >= 0.9.0
Provides:       crate(%{pkgname}/v0-3-33) = %{version}
Provides:       crate(%{pkgname}/v0-3-34) = %{version}
Provides:       crate(%{pkgname}/v0-3-39) = %{version}
Provides:       crate(%{pkgname}/v0-3-40) = %{version}
Provides:       crate(%{pkgname}/v0-3-41) = %{version}
Provides:       crate(%{pkgname}/v0-3-43) = %{version}
Provides:       crate(%{pkgname}/v0-3-44) = %{version}
Provides:       crate(%{pkgname}/v0-3-45) = %{version}
Provides:       crate(%{pkgname}/v0-3-49) = %{version}
Provides:       crate(%{pkgname}/v0-3-53) = %{version}
Provides:       crate(%{pkgname}/v0-3-57) = %{version}
Provides:       crate(%{pkgname}/v0-3-64) = %{version}

%description -n %{name}+v0-3-33
This metapackage enables feature "v0_3_33" for the Rust pipewire crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v0_3_34", "v0_3_39", "v0_3_40", "v0_3_41", "v0_3_43", "v0_3_44", "v0_3_45", "v0_3_49", "v0_3_53", "v0_3_57", and "v0_3_64" features.

%package     -n %{name}+v0-3-65
Summary:        Rust bindings for PipeWire - feature "v0_3_65" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v0-3-64) = %{version}
Requires:       crate(libspa-0.9/v0-3-65) >= 0.9.0
Provides:       crate(%{pkgname}/v0-3-65) = %{version}
Provides:       crate(%{pkgname}/v0-3-77) = %{version}

%description -n %{name}+v0-3-65
This metapackage enables feature "v0_3_65" for the Rust pipewire crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v0_3_77" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
