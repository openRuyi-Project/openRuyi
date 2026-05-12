# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap
%global full_version 4.6.0
%global pkgname clap-4.0

Name:           rust-clap-4.0
Version:        4.6.0
Release:        %autorelease
Summary:        Rust crate "clap"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:b193af5b67834b676abd72466a96c1024e6a6ad978a1f484bd90b85c94041351
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-builder-4.0) >= 4.6.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable-derive-ui-tests)

%description
Source code for takopackized Rust crate "clap"

%package     -n %{name}+cargo
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "cargo"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/cargo) >= 4.6.0
Provides:       crate(%{pkgname}/cargo)

%description -n %{name}+cargo
This metapackage enables feature "cargo" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "color"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/color) >= 4.6.0
Provides:       crate(%{pkgname}/color)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/debug) >= 4.6.0
Requires:       crate(clap-derive-4.0/debug) >= 4.6.0
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

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
This metapackage enables feature "default" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deprecated
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "deprecated"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/deprecated) >= 4.6.0
Requires:       crate(clap-derive-4.0/deprecated) >= 4.6.0
Provides:       crate(%{pkgname}/deprecated)

%description -n %{name}+deprecated
This metapackage enables feature "deprecated" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(clap-derive-4.0/default) >= 4.6.0
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "env"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/env) >= 4.6.0
Provides:       crate(%{pkgname}/env)

%description -n %{name}+env
This metapackage enables feature "env" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+error-context
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "error-context"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/error-context) >= 4.6.0
Provides:       crate(%{pkgname}/error-context)

%description -n %{name}+error-context
This metapackage enables feature "error-context" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "help"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/help) >= 4.6.0
Provides:       crate(%{pkgname}/help)

%description -n %{name}+help
This metapackage enables feature "help" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/std) >= 4.6.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+string
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "string"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/string) >= 4.6.0
Provides:       crate(%{pkgname}/string)

%description -n %{name}+string
This metapackage enables feature "string" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+suggestions
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "suggestions"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/suggestions) >= 4.6.0
Provides:       crate(%{pkgname}/suggestions)

%description -n %{name}+suggestions
This metapackage enables feature "suggestions" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/unicode) >= 4.6.0
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-doc
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-doc"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/derive)
Requires:       crate(clap-builder-4.0/unstable-doc) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-doc)

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-ext
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-ext"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/unstable-ext) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-ext)

%description -n %{name}+unstable-ext
This metapackage enables feature "unstable-ext" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-markdown
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-markdown"
Requires:       crate(%{pkgname})
Requires:       crate(clap-derive-4.0/unstable-markdown) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-markdown)

%description -n %{name}+unstable-markdown
This metapackage enables feature "unstable-markdown" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-styles
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-styles"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/unstable-styles) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-styles)

%description -n %{name}+unstable-styles
This metapackage enables feature "unstable-styles" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-v5
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-v5"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/deprecated)
Requires:       crate(clap-builder-4.0/unstable-v5) >= 4.6.0
Requires:       crate(clap-derive-4.0/unstable-v5) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-v5)

%description -n %{name}+unstable-v5
This metapackage enables feature "unstable-v5" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+usage
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "usage"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/usage) >= 4.6.0
Provides:       crate(%{pkgname}/usage)

%description -n %{name}+usage
This metapackage enables feature "usage" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wrap-help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "wrap_help"
Requires:       crate(%{pkgname})
Requires:       crate(clap-builder-4.0/wrap-help) >= 4.6.0
Provides:       crate(%{pkgname}/wrap-help)

%description -n %{name}+wrap-help
This metapackage enables feature "wrap_help" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
