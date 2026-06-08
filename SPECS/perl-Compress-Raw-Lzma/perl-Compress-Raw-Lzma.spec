# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Compress-Raw-Lzma
Version:        2.221
Release:        %autorelease
Summary:        Low-Level Perl Interface to lzma compression library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Compress-Raw-Lzma
#!RemoteAsset:  sha256:e8b2d17c7f29b3e4f286cc3d3f5353df8e811615c42298eedad7cdbfec4aed7f
Source0:        https://www.cpan.org/authors/id/P/PM/PMQS/Compress-Raw-Lzma-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  pkgconfig(liblzma)

%description
Compress::Raw::Lzma provides an interface to the in-memory
compression/uncompression functions from the lzma compression library.

%files -f %{name}.files
%doc Changes README SECURITY.md

%changelog
%autochangelog
