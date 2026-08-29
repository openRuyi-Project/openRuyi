# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name built
%global full_version 0.8.1
%global pkgname built-0.8

Name:           rust-built-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "built"
License:        MIT
URL:            https://github.com/lukaslueg/built
#!RemoteAsset:  sha256:5c0e531d93d39c34eef561e929e8a7f86d77a5af08aac4f6d6e39976c51858e9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "built"

%package     -n %{name}+cargo-lock
Summary:        Provides a crate with information from the time it was built - feature "cargo-lock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-lock-11) >= 11.0.0
Provides:       crate(%{pkgname}/cargo-lock) = %{version}

%description -n %{name}+cargo-lock
This metapackage enables feature "cargo-lock" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Provides a crate with information from the time it was built - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dependency-tree
Summary:        Provides a crate with information from the time it was built - feature "dependency-tree"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-lock-11/dependency-tree) >= 11.0.0
Provides:       crate(%{pkgname}/dependency-tree) = %{version}

%description -n %{name}+dependency-tree
This metapackage enables feature "dependency-tree" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+git2
Summary:        Provides a crate with information from the time it was built - feature "git2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(git2-0.21) >= 0.21.0
Provides:       crate(%{pkgname}/git2) = %{version}

%description -n %{name}+git2
This metapackage enables feature "git2" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix
Summary:        Provides a crate with information from the time it was built - feature "gix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-0.83/max-performance-safe) >= 0.83.0
Requires:       crate(gix-0.83/revision) >= 0.83.0
Requires:       crate(gix-0.83/sha1) >= 0.83.0
Requires:       crate(gix-0.83/status) >= 0.83.0
Provides:       crate(%{pkgname}/gix) = %{version}

%description -n %{name}+gix
This metapackage enables feature "gix" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+semver
Summary:        Provides a crate with information from the time it was built - feature "semver"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(semver-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/semver) = %{version}

%description -n %{name}+semver
This metapackage enables feature "semver" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
