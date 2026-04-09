# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           which
Version:        2.23
Release:        %autorelease
Summary:        Displays where a particular program in your path is located
License:        GPL-3.0-or-later
URL:            https://savannah.gnu.org/projects/which/
VCS:            git:https://https.git.savannah.gnu.org/git/which.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/which/which-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/which/which-%{version}.tar.gz.sig
#!RemoteAsset
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=3639#/which.keyring
BuildSystem:    autotools

Provides:       util-linux:%{_bindir}/which

%description
The which command shows the full pathname of a specified program, if the
specified program is in your PATH.

%files
%license COPYING
%doc EXAMPLES README README.alias AUTHORS NEWS
%{_bindir}/which
%{_infodir}/which.info*
%{_mandir}/man1/which.1*

%changelog
%autochangelog
