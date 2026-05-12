# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_builder
%global full_version 4.6.0
%global pkgname clap-builder-4.0

Name:           rust-clap-builder-4.0
Version:        4.6.0
Release:        %autorelease
Summary:        Rust crate "clap_builder"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:714a53001bf66416adb0e2ef5ac857140e7dc3a0c48fb28b2f10762fc4b5069f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(clap-lex-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cargo)
Provides:       crate(%{pkgname}/deprecated)
Provides:       crate(%{pkgname}/env)
Provides:       crate(%{pkgname}/error-context)
Provides:       crate(%{pkgname}/help)
Provides:       crate(%{pkgname}/string)
Provides:       crate(%{pkgname}/unstable-ext)
Provides:       crate(%{pkgname}/unstable-v5)
Provides:       crate(%{pkgname}/usage)

%description
Source code for takopackized Rust crate "clap_builder"

%package     -n %{name}+color
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "color" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(anstream-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/color)
Provides:       crate(%{pkgname}/unstable-styles)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-styles" feature.

%package     -n %{name}+debug
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(backtrace-0.3/default) >= 0.3.76
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/color)
Requires:       crate(%{pkgname}/error-context)
Requires:       crate(%{pkgname}/help)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/suggestions)
Requires:       crate(%{pkgname}/usage)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(anstyle-1.0/std) >= 1.0.14
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+suggestions
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "suggestions"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/error-context)
Requires:       crate(strsim-0.11/default) >= 0.11.1
Provides:       crate(%{pkgname}/suggestions)

%description -n %{name}+suggestions
This metapackage enables feature "suggestions" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(unicase-2.0/default) >= 2.9.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-doc
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-doc"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cargo)
Requires:       crate(%{pkgname}/env)
Requires:       crate(%{pkgname}/string)
Requires:       crate(%{pkgname}/unicode)
Requires:       crate(%{pkgname}/unstable-ext)
Requires:       crate(%{pkgname}/wrap-help)
Provides:       crate(%{pkgname}/unstable-doc)

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wrap-help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "wrap_help"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/help)
Requires:       crate(terminal-size-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/wrap-help)

%description -n %{name}+wrap-help
This metapackage enables feature "wrap_help" for the Rust clap_builder crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
