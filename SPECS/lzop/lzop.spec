# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lzop
Version:        1.04
Release:        %autorelease
Summary:        A fast LZ-based file compressor
License:        GPL-2.0-or-later
URL:            https://www.lzop.org/
# VCS: No VCS link available
#!RemoteAsset
Source:         https://www.lzop.org/download/lzop-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lzo2)

%description
lzop is a file compressor which is very similar to gzip. lzop favors speed over
compression ratio.

lzop was designed with the following goals in mind:
- Speed (both compression and decompression)
- Reasonable drop-in compatibility to gzip
- Portability

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING
%{_bindir}/lzop
%{_mandir}/man1/lzop.1*
%doc %{_docdir}/lzop

%changelog
%autochangelog
