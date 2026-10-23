# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ultraviolet
%define go_import_path  github.com/charmbracelet/ultraviolet

Name:           go-github-charmbracelet-ultraviolet
Version:        0+git20261022.6b8d4ba
Release:        %autorelease
Summary:        Terminal rendering and input primitives for Go
License:        MIT
URL:            https://github.com/charmbracelet/ultraviolet
#!RemoteAsset:  sha256:75e4109504bd3e265e6a220eead7714f6be2ba0196d7fdea3b3903f91ef907bd
Source0:        https://codeload.github.com/charmbracelet/ultraviolet/tar.gz/6b8d4baf91b4c933e6613b0eefc8f180f6eda002#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(charm.land/lipgloss/v2)
BuildRequires:  go(github.com/bits-and-blooms/bitset)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/ansi/iterm2)
BuildRequires:  go(github.com/charmbracelet/x/ansi/kitty)
BuildRequires:  go(github.com/charmbracelet/x/ansi/parser)
BuildRequires:  go(github.com/charmbracelet/x/ansi/sixel)
BuildRequires:  go(github.com/charmbracelet/x/exp/ordered)
BuildRequires:  go(github.com/charmbracelet/x/mosaic)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/charmbracelet/x/termios)
BuildRequires:  go(github.com/charmbracelet/x/vt)
BuildRequires:  go(github.com/charmbracelet/x/windows)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/clipperhouse/uax29/v2/graphemes)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(go.mitchellh.com/libghostty)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/errgroup)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)
BuildRequires:  go(golang.org/x/sys/windows)

# Export the source module roots and every installed Go package.
Provides:       go(examples) = %{version}
Provides:       go(examples/advanced/boxes) = %{version}
Provides:       go(examples/advanced/image) = %{version}
Provides:       go(examples/advanced/layout) = %{version}
Provides:       go(examples/advanced/rgbimage) = %{version}
Provides:       go(examples/advanced/space) = %{version}
Provides:       go(examples/advanced/splits) = %{version}
Provides:       go(examples/advanced/tv) = %{version}
Provides:       go(examples/altscreen) = %{version}
Provides:       go(examples/draw) = %{version}
Provides:       go(examples/helloworld) = %{version}
Provides:       go(examples/mouse) = %{version}
Provides:       go(examples/panic) = %{version}
Provides:       go(examples/prependline) = %{version}
Provides:       go(examples/widths) = %{version}
Provides:       go(github.com/charmbracelet/ultraviolet) = %{version}
Provides:       go(github.com/charmbracelet/ultraviolet/internal/casso) = %{version}
Provides:       go(github.com/charmbracelet/ultraviolet/internal/conformance) = %{version}
Provides:       go(github.com/charmbracelet/ultraviolet/internal/lru) = %{version}
Provides:       go(github.com/charmbracelet/ultraviolet/layout) = %{version}
Provides:       go(github.com/charmbracelet/ultraviolet/screen) = %{version}

Requires:       go(charm.land/lipgloss/v2)
Requires:       go(github.com/charmbracelet/colorprofile)
Requires:       go(github.com/charmbracelet/x/ansi)
Requires:       go(github.com/charmbracelet/x/ansi/iterm2)
Requires:       go(github.com/charmbracelet/x/ansi/kitty)
Requires:       go(github.com/charmbracelet/x/ansi/parser)
Requires:       go(github.com/charmbracelet/x/ansi/sixel)
Requires:       go(github.com/charmbracelet/x/mosaic)
Requires:       go(github.com/charmbracelet/x/term)
Requires:       go(github.com/charmbracelet/x/termios)
Requires:       go(github.com/charmbracelet/x/windows)
Requires:       go(github.com/clipperhouse/uax29/v2/graphemes)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/muesli/cancelreader)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(github.com/xo/terminfo)
Requires:       go(golang.org/x/sync/errgroup)
Requires:       go(golang.org/x/sys/unix)
Requires:       go(golang.org/x/sys/windows)

%description
Terminal rendering and input primitives for Go. This package contains the
complete upstream repository sources and tests.

%prep
%autosetup -n ultraviolet-6b8d4baf91b4c933e6613b0eefc8f180f6eda002

# Nested modules use their declared import paths in the GOPATH test tree.
%check -p
%go_common
mkdir -p %{_builddir}/go/src/examples
cp -a examples/. %{_builddir}/go/src/examples/

# Install independent module roots at their real import paths.
%install -a
mkdir -p %{buildroot}%{go_sys_gopath}/examples
cp -a examples/. %{buildroot}%{go_sys_gopath}/examples/

# Exercise every non-fixture nested module as well as the root module.
%check -a
%go_common
pushd %{_builddir}/go/src/examples
%{__go} test %{go_test_flags_default} ./...
popd
pushd %{_builddir}/go/src/github.com/charmbracelet/ultraviolet/internal/conformance
%{__go} test %{go_test_flags_default} ./...
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/examples

%changelog
%autochangelog
