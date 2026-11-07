# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap
%global full_version 2.34.0
%global pkgname clap-2

Name:           rust-clap-2
Version:        2.34.0
Release:        %autorelease
Summary:        Rust crate "clap"
License:        MIT
URL:            https://clap.rs/
#!RemoteAsset:  sha256:a0610544180c38b88101fecf2dd634b174a62eef6946f84dfc6a7127512b381c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(textwrap-0.11/default) >= 0.11.0
Requires:       crate(unicode-width-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/no-cargo) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "clap"

%package     -n %{name}+ansi-term
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "ansi_term"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ansi-term-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/ansi-term) = %{version}

%description -n %{name}+ansi-term
This metapackage enables feature "ansi_term" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+atty
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "atty"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atty-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/atty) = %{version}

%description -n %{name}+atty
This metapackage enables feature "atty" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clippy
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.166/default) >= 0.0.166
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ansi-term) = %{version}
Requires:       crate(%{pkgname}/atty) = %{version}
Provides:       crate(%{pkgname}/color) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color) = %{version}
Requires:       crate(%{pkgname}/suggestions) = %{version}
Requires:       crate(%{pkgname}/vec-map) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strsim
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "strsim" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(strsim-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/strsim) = %{version}
Provides:       crate(%{pkgname}/suggestions) = %{version}

%description -n %{name}+strsim
This metapackage enables feature "strsim" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "suggestions" feature.

%package     -n %{name}+term-size
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "term_size"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(term-size-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/term-size) = %{version}

%description -n %{name}+term-size
This metapackage enables feature "term_size" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vec-map
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "vec_map"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vec-map-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/vec-map) = %{version}

%description -n %{name}+vec-map
This metapackage enables feature "vec_map" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wrap-help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "wrap_help"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/term-size) = %{version}
Requires:       crate(textwrap-0.11/term-size) >= 0.11.0
Provides:       crate(%{pkgname}/wrap-help) = %{version}

%description -n %{name}+wrap-help
This metapackage enables feature "wrap_help" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yaml-rust
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "yaml-rust" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(yaml-rust-0.3/default) >= 0.3.5
Provides:       crate(%{pkgname}/doc) = %{version}
Provides:       crate(%{pkgname}/yaml) = %{version}
Provides:       crate(%{pkgname}/yaml-rust) = %{version}

%description -n %{name}+yaml-rust
This metapackage enables feature "yaml-rust" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "doc", and "yaml" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
