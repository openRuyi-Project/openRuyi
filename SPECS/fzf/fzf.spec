# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define go_import_path  github.com/junegunn/fzf

Name:           fzf
Version:        0.72.0
Release:        %autorelease
Summary:        Command-line fuzzy finder
License:        MIT
URL:            https://github.com/junegunn/fzf
#!RemoteAsset:  sha256:ca5ce083cec5187503ceb96d837c20d8efde85f03e62bba3a8890f8da526f2fc
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  -C %{_builddir}/go/src/%{go_import_path}
BuildOption(build):  FZF_VERSION=%{version}
BuildOption(build):  FZF_REVISION=tarball
BuildOption(build):  install

BuildRequires:  go >= 1.23
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  go(github.com/charlievieth/fastwalk)
BuildRequires:  go(github.com/gdamore/encoding)
BuildRequires:  go(github.com/gdamore/tcell/v2)
BuildRequires:  go(github.com/junegunn/go-shellwords)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Requires:       bash
Recommends:     tmux

%description
fzf is a general-purpose command-line fuzzy finder. It can interactively filter
files, command history, processes, host names, bookmarks, git commits, and other
line-oriented input.

%conf
# No configuration needed.

%build -p
%go_common
export GOFLAGS="-buildmode=pie -trimpath -buildvcs=false"
mkdir -p %{_builddir}/go/src/github.com/junegunn
# GOPATH mode lets the build use packaged Go dependency sources
ln -snf "$(pwd)" %{_builddir}/go/src/%{go_import_path}

# upstream %install only install bin/fzf
%install
install -D -m 0755 bin/fzf %{buildroot}%{_bindir}/fzf
install -D -m 0755 bin/fzf-preview.sh %{buildroot}%{_bindir}/fzf-preview.sh
install -D -m 0755 bin/fzf-tmux %{buildroot}%{_bindir}/fzf-tmux
install -D -m 0644 man/man1/fzf.1 %{buildroot}%{_mandir}/man1/fzf.1
install -D -m 0644 man/man1/fzf-tmux.1 %{buildroot}%{_mandir}/man1/fzf-tmux.1

%check
%go_common
export GOFLAGS="-buildmode=pie -trimpath -buildvcs=false"
%__make -C %{_builddir}/go/src/%{go_import_path} FZF_VERSION=%{version} FZF_REVISION=tarball test

%files
%doc ADVANCED.md BUILD.md CHANGELOG.md README.md README-VIM.md doc/fzf.txt
%license LICENSE
%{_bindir}/fzf
%{_bindir}/fzf-preview.sh
%{_bindir}/fzf-tmux
%{_mandir}/man1/fzf.1*
%{_mandir}/man1/fzf-tmux.1*

%changelog
%autochangelog
