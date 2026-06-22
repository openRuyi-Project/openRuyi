# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap
%global full_version 3.2.25
%global pkgname clap-3

Name:           rust-clap-3
Version:        3.2.25
Release:        %autorelease
Summary:        Rust crate "clap"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:4ea181bf566f71cb9a5d17a59e1871af638180a18fb0035c92ae62b705207123
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.2.0
Requires:       crate(clap-lex-0.2/default) >= 0.2.2
Requires:       crate(indexmap-1/default) >= 1.0.0
Requires:       crate(textwrap-0.16) >= 0.16.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/env) = %{version}
Provides:       crate(%{pkgname}/unstable-grouped) = %{version}
Provides:       crate(%{pkgname}/unstable-replace) = %{version}

%description
Source code for takopackized Rust crate "clap"

%package     -n %{name}+atty
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "atty"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atty-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/atty) = %{version}

%description -n %{name}+atty
This metapackage enables feature "atty" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backtrace
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap-derive
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "clap_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-derive-3/default) >= 3.2.25
Provides:       crate(%{pkgname}/clap-derive) = %{version}

%description -n %{name}+clap-derive
This metapackage enables feature "clap_derive" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/atty) = %{version}
Requires:       crate(%{pkgname}/termcolor) = %{version}
Provides:       crate(%{pkgname}/color) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backtrace) = %{version}
Requires:       crate(clap-derive-3/debug) >= 3.2.25
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/suggestions) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deprecated
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "deprecated"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-derive-3/deprecated) >= 3.2.25
Provides:       crate(%{pkgname}/deprecated) = %{version}

%description -n %{name}+deprecated
This metapackage enables feature "deprecated" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clap-derive) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "once_cell" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/cargo) = %{version}
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cargo" feature.

%package     -n %{name}+regex
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strsim
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "strsim" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(strsim-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/strsim) = %{version}
Provides:       crate(%{pkgname}/suggestions) = %{version}

%description -n %{name}+strsim
This metapackage enables feature "strsim" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "suggestions" feature.

%package     -n %{name}+termcolor
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "termcolor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termcolor-1/default) >= 1.1.1
Provides:       crate(%{pkgname}/termcolor) = %{version}

%description -n %{name}+termcolor
This metapackage enables feature "termcolor" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+terminal-size
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "terminal_size"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(terminal-size-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/terminal-size) = %{version}

%description -n %{name}+terminal-size
This metapackage enables feature "terminal_size" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.6.0
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unicase) = %{version}
Requires:       crate(textwrap-0.16/unicode-width) >= 0.16.0
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-doc
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cargo) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/env) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Requires:       crate(%{pkgname}/unstable-grouped) = %{version}
Requires:       crate(%{pkgname}/unstable-replace) = %{version}
Requires:       crate(%{pkgname}/wrap-help) = %{version}
Requires:       crate(%{pkgname}/yaml) = %{version}
Provides:       crate(%{pkgname}/unstable-doc) = %{version}

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-v4
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "unstable-v4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deprecated) = %{version}
Requires:       crate(clap-derive-3/unstable-v4) >= 3.2.25
Provides:       crate(%{pkgname}/unstable-v4) = %{version}

%description -n %{name}+unstable-v4
This metapackage enables feature "unstable-v4" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wrap-help
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "wrap_help"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/terminal-size) = %{version}
Requires:       crate(textwrap-0.16/terminal-size) >= 0.16.0
Provides:       crate(%{pkgname}/wrap-help) = %{version}

%description -n %{name}+wrap-help
This metapackage enables feature "wrap_help" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yaml-rust
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser - feature "yaml-rust" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(yaml-rust-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/yaml) = %{version}
Provides:       crate(%{pkgname}/yaml-rust) = %{version}

%description -n %{name}+yaml-rust
This metapackage enables feature "yaml-rust" for the Rust clap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "yaml" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
