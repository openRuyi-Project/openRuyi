# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ed
Version:        1.22.5
Release:        %autorelease
Summary:        A line-oriented text editor
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnu.org/software/ed/
# VCS: TODO: How to write https://savannah.gnu.org/cvs/?group=ed
#!RemoteAsset:  sha256:56e107ddc2f29dad6690376c15bf9751509e1ee3b8241710e44edbe5c3a158cc
Source:         https://ftpmirror.gnu.org/ed/ed-%{version}.tar.lz
Buildsystem:    autotools

BuildRequires:  lzip

%description
GNU ed is a line-oriented text editor. It is used to create, display,
modify and otherwise manipulate text files, both interactively and via
shell scripts. A restricted version of ed, red, can only edit files in
the current directory and cannot execute shell commands. Ed is the
"standard" text editor in the sense that it is the original editor for
Unix, and thus widely available. For most purposes, however, it is
superseded by full-screen editors such as GNU Emacs or GNU Moe.

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_bindir}/r%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/r%{name}.1%{?ext_man}

%changelog
%autochangelog
