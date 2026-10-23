# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lipgloss
%define go_import_path  charm.land/lipgloss/v2

Name:           go-charm-lipgloss-v2
Version:        2.0.6
Release:        %autorelease
Summary:        Terminal styling and layout library for Go
License:        MIT
URL:            https://github.com/charmbracelet/lipgloss
#!RemoteAsset:  sha256:18ea296fe5cda5e93114f988e820106620aa8d38f3435276e8fe6ab726f04922
Source0:        https://github.com/charmbracelet/lipgloss/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n lipgloss-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(charm.land/bubbletea/v2)
BuildRequires:  go(github.com/anmitsu/go-shlex)
BuildRequires:  go(github.com/aymanbagabas/go-udiff)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/keygen)
BuildRequires:  go(github.com/charmbracelet/log/v2)
BuildRequires:  go(github.com/charmbracelet/ssh)
BuildRequires:  go(github.com/charmbracelet/ultraviolet)
BuildRequires:  go(github.com/charmbracelet/wish/v2)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/conpty)
BuildRequires:  go(github.com/charmbracelet/x/errors)
BuildRequires:  go(github.com/charmbracelet/x/exp/charmtone)
BuildRequires:  go(github.com/charmbracelet/x/exp/golden)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/charmbracelet/x/termios)
BuildRequires:  go(github.com/charmbracelet/x/windows)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(charm.land/lipgloss/v2) = %{version}
Provides:       go(charm.land/lipgloss/v2/compat) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/blending/border-blend-rotation/bubbletea) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/blending/linear-1d/bubbletea) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/blending/linear-1d/standalone) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/blending/linear-2d/bubbletea) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/blending/linear-2d/standalone) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/brightness) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/canvas) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/color/bubbletea) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/color/standalone) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/compat/bubbletea) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/compat/standalone) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/layout) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/list/duckduckgoose) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/list/glow) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/list/grocery) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/list/roman) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/list/simple) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/list/sublist) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/ssh) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/table/ansi) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/table/chess) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/table/languages) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/table/mindy) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/table/pokemon) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/background) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/files) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/makeup) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/rounded) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/selection) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/simple) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/styles) = %{version}
Provides:       go(charm.land/lipgloss/v2/examples/tree/toggle) = %{version}
Provides:       go(charm.land/lipgloss/v2/list) = %{version}
Provides:       go(charm.land/lipgloss/v2/table) = %{version}
Provides:       go(charm.land/lipgloss/v2/tree) = %{version}

Requires:       go(charm.land/bubbletea/v2)
Requires:       go(github.com/charmbracelet/colorprofile)
Requires:       go(github.com/charmbracelet/ssh)
Requires:       go(github.com/charmbracelet/ultraviolet)
Requires:       go(github.com/charmbracelet/wish/v2)
Requires:       go(github.com/charmbracelet/x/ansi)
Requires:       go(github.com/charmbracelet/x/exp/charmtone)
Requires:       go(github.com/charmbracelet/x/term)
Requires:       go(github.com/clipperhouse/displaywidth)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(golang.org/x/sys)

%description
Terminal styling and layout library for Go.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
