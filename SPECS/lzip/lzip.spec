# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lzip
Version:        1.25
Release:        %autorelease
Summary:        Lossless file compressor based on the LZMA algorithm
License:        GPL-3.0-or-later
URL:            https://www.nongnu.org/lzip/lzip.html
# VCS: TODO: cvs -z3 -d:pserver:anonymous@cvs.savannah.nongnu.org:/sources/lzip co lzip
#!RemoteAsset
Source:         https://download.savannah.nongnu.org/releases/lzip/lzip-%{version}.tar.gz
Buildsystem:    autotools

BuildRequires:  gcc-c++

%description
Lzip is a lossless file compressor based on the LZMA (Lempel-Ziv-Markov
chain-Algorithm) algorithm.
 The high compression of LZMA comes from
combining two basic, well-proven compression ideas: sliding dictionaries
(i.e. LZ77/78), and markov models (i.e. the thing used by every
compression algorithm that uses a range encoder or similar order-0
entropy coder as its last stage) with segregation of contexts according
to what the bits are used for.

Lzip is not a replacement for gzip or bzip2, but a complement; which
one is best to use depends on user's needs. Gzip is the fastest and most
widely used. Bzip2 compresses better than gzip but is slower, both
compressing and decompressing.
Lzip decompresses almost as fast as gzip
and compresses better than bzip2, but requires more memory and time
during compression. These features make lzip well suited for software
distribution and data archival.

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
%autochangelog
