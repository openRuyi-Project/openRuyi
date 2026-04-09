# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sshpass
Version:        1.10
Release:        %autorelease
Summary:        Non-interactive SSH authentication utility
License:        GPL-2.0-or-later
URL:            http://sshpass.sourceforge.net/
VCS:            svn:https://svn.code.sf.net/p/sshpass/code/trunk
#!RemoteAsset
Source0:        https://downloads.sourceforge.net/project/sshpass/sshpass/1.10/sshpass-1.10.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc

%description
sshpass is a tool for non-interactively performing password authentication
with SSH's "interactive keyboard password authentication". Most users should
use the more secure public key authentication method instead.

%files
%doc AUTHORS COPYING ChangeLog NEWS
%{_bindir}/sshpass
%{_mandir}/man1/sshpass.1*

%changelog
%autochangelog
