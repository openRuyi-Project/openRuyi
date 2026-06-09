# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Compress-Brotli
Version:        0.022
Release:        %autorelease
Summary:        Write Brotli buffers/streams
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Compress-Brotli
#!RemoteAsset:  sha256:364d2f4131548d6fac5f2df7750d0bd8ebfee10a7c28eb05e7b98ce6ac7facc1
Source0:        https://www.cpan.org/authors/id/T/TI/TIMLEGGE/IO-Compress-Brotli-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  cmake
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Alien::cmake3)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Time::HiRes)

%description
IO::Compress::Brotli is a module that compressed Brotli buffers and
streams. Despite its name, it is not a subclass of IO::Compress::Base
and does not implement its interface. This will be rectified in a
future release.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
