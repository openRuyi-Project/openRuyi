# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tree
Version:        2.3.2
Release:        %autorelease
Summary:        File system tree viewer
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://oldmanprogrammer.net/source.php?dir=projects/tree
VCS:            git:https://github.com/Old-Man-Programmer/tree
#!RemoteAsset:  sha256:22cf32e84e3eb508d97a9e991c2c3cc006b9dcf4afed201d96311c5c57d08fcf
Source0:        https://github.com/Old-Man-Programmer/tree/archive/%{version}/tree-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  DESTDIR=%{buildroot}%{_bindir}
BuildOption(install):  MANDIR=%{buildroot}%{_mandir}

BuildRequires:  make

%description
Tree is a recursive directory listing command that produces a depth
indented listing of files, which is colorized ala dircolors if the
LS_COLORS environment variable is set and output is to tty.

# No conf
%conf

%build -p
%set_build_flags

# No check
%check

%files
%license LICENSE
%doc README
%{_bindir}/tree
%{_mandir}/man1/tree.1*

%changelog
%autochangelog
