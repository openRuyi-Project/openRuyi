# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           augeas
Version:        1.14.1
Release:        %autorelease
Summary:        A library for changing configuration files
License:        LGPL-2.1-or-later
URL:            https://augeas.net/
VCS:            git:https://github.com/hercules-team/augeas
#!RemoteAsset
Source0:        https://github.com/hercules-team/augeas/releases/download/release-%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-silent-rules

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  bash-completion

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package       bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion
Requires:      %{name} = %{version}-%{release}

%description   bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.

%ifarch riscv64
# TODO: make tests pass.
%check
%endif

%files
%license COPYING
%doc AUTHORS NEWS
%doc %{_mandir}/man1/*
%{_bindir}/augmatch
%{_bindir}/augparse
%{_bindir}/augprint
%{_bindir}/augtool
%{_bindir}/fadot
%{_datadir}/augeas/lenses/dist
%{_datadir}/vim/vimfiles/syntax/augeas.vim
%{_datadir}/vim/vimfiles/ftdetect/augeas.vim
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc

%files bash-completion
%{bash_completions_dir}/augmatch
%{bash_completions_dir}/augprint
%{bash_completions_dir}/augtool

%changelog
%{?autochangelog}
