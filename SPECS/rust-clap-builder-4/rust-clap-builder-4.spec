# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_builder
%global full_version 4.6.0
%global pkgname clap-builder-4

Name:           rust-clap-builder-4
Version:        4.6.0
Release:        %autorelease
Summary:        Rust crate "clap_builder"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:714a53001bf66416adb0e2ef5ac857140e7dc3a0c48fb28b2f10762fc4b5069f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.13
Requires:       crate(clap-lex-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cargo) = %{version}
Provides:       crate(%{pkgname}/deprecated) = %{version}
Provides:       crate(%{pkgname}/env) = %{version}
Provides:       crate(%{pkgname}/error-context) = %{version}
Provides:       crate(%{pkgname}/help) = %{version}
Provides:       crate(%{pkgname}/string) = %{version}
Provides:       crate(%{pkgname}/unstable-ext) = %{version}
Provides:       crate(%{pkgname}/unstable-v5) = %{version}
Provides:       crate(%{pkgname}/usage) = %{version}

%description
Source code for takopackized Rust crate "clap_builder"

%package     -n %{name}+color
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "color" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstream-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/color) = %{version}
Provides:       crate(%{pkgname}/unstable-styles) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-styles" feature.

%package     -n %{name}+debug
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.76
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color) = %{version}
Requires:       crate(%{pkgname}/error-context) = %{version}
Requires:       crate(%{pkgname}/help) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/suggestions) = %{version}
Requires:       crate(%{pkgname}/usage) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-1/std) >= 1.0.13
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+suggestions
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "suggestions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/error-context) = %{version}
Requires:       crate(strsim-0.11/default) >= 0.11.1
Provides:       crate(%{pkgname}/suggestions) = %{version}

%description -n %{name}+suggestions
This metapackage enables feature "suggestions" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.9.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-doc
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cargo) = %{version}
Requires:       crate(%{pkgname}/env) = %{version}
Requires:       crate(%{pkgname}/string) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Requires:       crate(%{pkgname}/unstable-ext) = %{version}
Requires:       crate(%{pkgname}/wrap-help) = %{version}
Provides:       crate(%{pkgname}/unstable-doc) = %{version}

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wrap-help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "wrap_help"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/help) = %{version}
Requires:       crate(terminal-size-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/wrap-help) = %{version}

%description -n %{name}+wrap-help
This metapackage enables feature "wrap_help" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
