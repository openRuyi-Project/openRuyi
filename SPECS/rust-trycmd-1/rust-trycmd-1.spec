# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name trycmd
%global full_version 1.0.2
%global pkgname trycmd-1

Name:           rust-trycmd-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "trycmd"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/snapbox/
#!RemoteAsset:  sha256:b540f821f2e33b85807ad6307849edd96e6b09bf8b687b3c52adeaa1a340be1f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(automod-1/default) >= 1.0.15
Requires:       crate(glob-0.3/default) >= 0.3.3
Requires:       crate(humantime-2/default) >= 2.0.0
Requires:       crate(humantime-serde-1/default) >= 1.0.0
Requires:       crate(rayon-1/default) >= 1.10.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(shlex-1/default) >= 1.3.0
Requires:       crate(snapbox-1/cmd) >= 1.0.2
Requires:       crate(toml-edit-0.23/default) >= 0.23.5
Requires:       crate(toml-edit-0.23/serde) >= 0.23.5

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "trycmd"

%package     -n %{name}+color
Summary:        Snapshot testing for a herd of CLI tests - feature "color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstream-1/default) >= 1.0.0
Requires:       crate(snapbox-1/cmd) >= 1.0.2
Requires:       crate(snapbox-1/color) >= 1.0.2
Provides:       crate(%{pkgname}/color) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color-auto
Summary:        Snapshot testing for a herd of CLI tests - feature "color-auto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color) = %{version}
Requires:       crate(snapbox-1/cmd) >= 1.0.2
Requires:       crate(snapbox-1/color-auto) >= 1.0.2
Provides:       crate(%{pkgname}/color-auto) = %{version}

%description -n %{name}+color-auto
This metapackage enables feature "color-auto" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Snapshot testing for a herd of CLI tests - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snapbox-1/cmd) >= 1.0.2
Requires:       crate(snapbox-1/debug) >= 1.0.2
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Snapshot testing for a herd of CLI tests - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color-auto) = %{version}
Requires:       crate(%{pkgname}/diff) = %{version}
Requires:       crate(%{pkgname}/filesystem) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diff
Summary:        Snapshot testing for a herd of CLI tests - feature "diff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snapbox-1/cmd) >= 1.0.2
Requires:       crate(snapbox-1/diff) >= 1.0.2
Provides:       crate(%{pkgname}/diff) = %{version}

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+escargot
Summary:        Snapshot testing for a herd of CLI tests - feature "escargot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(escargot-0.5/default) >= 0.5.14
Provides:       crate(%{pkgname}/escargot) = %{version}

%description -n %{name}+escargot
This metapackage enables feature "escargot" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+examples
Summary:        Snapshot testing for a herd of CLI tests - feature "examples"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snapbox-1/cmd) >= 1.0.2
Requires:       crate(snapbox-1/examples) >= 1.0.2
Provides:       crate(%{pkgname}/examples) = %{version}

%description -n %{name}+examples
This metapackage enables feature "examples" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filesystem
Summary:        Snapshot testing for a herd of CLI tests - feature "filesystem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snapbox-1/cmd) >= 1.0.2
Requires:       crate(snapbox-1/dir) >= 1.0.2
Provides:       crate(%{pkgname}/filesystem) = %{version}

%description -n %{name}+filesystem
This metapackage enables feature "filesystem" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schema
Summary:        Snapshot testing for a herd of CLI tests - feature "schema"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-0.8/default) >= 0.8.22
Requires:       crate(schemars-0.8/preserve-order) >= 0.8.22
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/schema) = %{version}

%description -n %{name}+schema
This metapackage enables feature "schema" for the Rust trycmd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
