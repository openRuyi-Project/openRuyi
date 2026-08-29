# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap
%global full_version 4.6.1
%global pkgname clap-4

Name:           rust-clap-4
Version:        4.6.1
Release:        %autorelease
Summary:        Rust crate "clap"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:1ddb117e43bbf7dacf0a4190fef4d345b9bad68dfc649cb349e7d17d28428e51
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-builder-4) >= 4.6.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable-derive-ui-tests) = %{version}

%description
Source code for takopackized Rust crate "clap"

%package     -n %{name}+cargo
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "cargo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/cargo) >= 4.6.0
Provides:       crate(%{pkgname}/cargo) = %{version}

%description -n %{name}+cargo
This metapackage enables feature "cargo" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/color) >= 4.6.0
Provides:       crate(%{pkgname}/color) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/debug) >= 4.6.0
Requires:       crate(clap-derive-4/debug) >= 4.6.1
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

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
This metapackage enables feature "default" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deprecated
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "deprecated"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/deprecated) >= 4.6.0
Requires:       crate(clap-derive-4/deprecated) >= 4.6.1
Provides:       crate(%{pkgname}/deprecated) = %{version}

%description -n %{name}+deprecated
This metapackage enables feature "deprecated" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-derive-4/default) >= 4.6.1
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "env"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/env) >= 4.6.0
Provides:       crate(%{pkgname}/env) = %{version}

%description -n %{name}+env
This metapackage enables feature "env" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+error-context
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "error-context"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/error-context) >= 4.6.0
Provides:       crate(%{pkgname}/error-context) = %{version}

%description -n %{name}+error-context
This metapackage enables feature "error-context" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "help"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/help) >= 4.6.0
Provides:       crate(%{pkgname}/help) = %{version}

%description -n %{name}+help
This metapackage enables feature "help" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/std) >= 4.6.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+string
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "string"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/string) >= 4.6.0
Provides:       crate(%{pkgname}/string) = %{version}

%description -n %{name}+string
This metapackage enables feature "string" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+suggestions
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "suggestions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/suggestions) >= 4.6.0
Provides:       crate(%{pkgname}/suggestions) = %{version}

%description -n %{name}+suggestions
This metapackage enables feature "suggestions" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/unicode) >= 4.6.0
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-doc
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(clap-builder-4/unstable-doc) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-doc) = %{version}

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-ext
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-ext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/unstable-ext) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-ext) = %{version}

%description -n %{name}+unstable-ext
This metapackage enables feature "unstable-ext" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-markdown
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-markdown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-derive-4/unstable-markdown) >= 4.6.1
Provides:       crate(%{pkgname}/unstable-markdown) = %{version}

%description -n %{name}+unstable-markdown
This metapackage enables feature "unstable-markdown" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-styles
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-styles"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/unstable-styles) >= 4.6.0
Provides:       crate(%{pkgname}/unstable-styles) = %{version}

%description -n %{name}+unstable-styles
This metapackage enables feature "unstable-styles" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-v5
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-v5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deprecated) = %{version}
Requires:       crate(clap-builder-4/unstable-v5) >= 4.6.0
Requires:       crate(clap-derive-4/unstable-v5) >= 4.6.1
Provides:       crate(%{pkgname}/unstable-v5) = %{version}

%description -n %{name}+unstable-v5
This metapackage enables feature "unstable-v5" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+usage
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "usage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/usage) >= 4.6.0
Provides:       crate(%{pkgname}/usage) = %{version}

%description -n %{name}+usage
This metapackage enables feature "usage" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wrap-help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "wrap_help"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-builder-4/wrap-help) >= 4.6.0
Provides:       crate(%{pkgname}/wrap-help) = %{version}

%description -n %{name}+wrap-help
This metapackage enables feature "wrap_help" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
