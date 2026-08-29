# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miette
%global full_version 5.10.0
%global pkgname miette-5

Name:           rust-miette-5
Version:        5.10.0
Release:        %autorelease
Summary:        Rust crate "miette"
License:        Apache-2.0
URL:            https://github.com/zkat/miette
#!RemoteAsset:  sha256:59bb584eaeeab6bd0226ccf3509a69d7936d148cf3d036ad350abe35e8c6856e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(miette-derive-5/default) >= 5.10.0
Requires:       crate(once-cell-1/default) >= 1.8.0
Requires:       crate(thiserror-1/default) >= 1.0.40
Requires:       crate(unicode-width-0.1/default) >= 0.1.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-format-args-capture) = %{version}

%description
Source code for takopackized Rust crate "miette"

%package     -n %{name}+backtrace
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.61
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+backtrace-ext
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "backtrace-ext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-ext-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/backtrace-ext) = %{version}

%description -n %{name}+backtrace-ext
This metapackage enables feature "backtrace-ext" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fancy
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "fancy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backtrace) = %{version}
Requires:       crate(%{pkgname}/backtrace-ext) = %{version}
Requires:       crate(%{pkgname}/fancy-no-backtrace) = %{version}
Provides:       crate(%{pkgname}/fancy) = %{version}

%description -n %{name}+fancy
This metapackage enables feature "fancy" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fancy-no-backtrace
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "fancy-no-backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/is-terminal) = %{version}
Requires:       crate(%{pkgname}/owo-colors) = %{version}
Requires:       crate(%{pkgname}/supports-color) = %{version}
Requires:       crate(%{pkgname}/supports-hyperlinks) = %{version}
Requires:       crate(%{pkgname}/supports-unicode) = %{version}
Requires:       crate(%{pkgname}/terminal-size) = %{version}
Requires:       crate(%{pkgname}/textwrap) = %{version}
Provides:       crate(%{pkgname}/fancy-no-backtrace) = %{version}

%description -n %{name}+fancy-no-backtrace
This metapackage enables feature "fancy-no-backtrace" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+is-terminal
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "is-terminal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(is-terminal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/is-terminal) = %{version}

%description -n %{name}+is-terminal
This metapackage enables feature "is-terminal" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+owo-colors
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "owo-colors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(owo-colors-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/owo-colors) = %{version}

%description -n %{name}+owo-colors
This metapackage enables feature "owo-colors" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.162
Requires:       crate(serde-1/derive) >= 1.0.162
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+supports-color
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "supports-color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(supports-color-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/supports-color) = %{version}

%description -n %{name}+supports-color
This metapackage enables feature "supports-color" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+supports-hyperlinks
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "supports-hyperlinks"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(supports-hyperlinks-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/supports-hyperlinks) = %{version}

%description -n %{name}+supports-hyperlinks
This metapackage enables feature "supports-hyperlinks" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+supports-unicode
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "supports-unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(supports-unicode-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/supports-unicode) = %{version}

%description -n %{name}+supports-unicode
This metapackage enables feature "supports-unicode" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+terminal-size
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "terminal_size"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(terminal-size-0.1/default) >= 0.1.17
Provides:       crate(%{pkgname}/terminal-size) = %{version}

%description -n %{name}+terminal-size
This metapackage enables feature "terminal_size" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+textwrap
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "textwrap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(textwrap-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/textwrap) = %{version}

%description -n %{name}+textwrap
This metapackage enables feature "textwrap" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
