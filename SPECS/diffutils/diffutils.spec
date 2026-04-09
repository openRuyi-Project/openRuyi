# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           diffutils
Version:        3.12
Release:        %autorelease
Summary:        GNU diff Utilities
License:        GFDL-1.2-only AND GPL-3.0-or-later
URL:            https://www.gnu.org/software/diffutils/
VCS:            git:https://https.git.savannah.gnu.org/git/diffutils.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
#!RemoteAsset
Source2:        https://savannah.gnu.org/project/release-gpgkeys.php?group=diffutils&download=1#/%{name}.keyring
BuildSystem:    autotools

%description
The GNU diff utilities find differences between files. diff is used to
make source code patches, for instance.

%install -a
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_bindir}/*
%{_infodir}/diffutils.info%{?ext_info}
%{_mandir}/man1/*.1%{?ext_man}

%changelog
%autochangelog
