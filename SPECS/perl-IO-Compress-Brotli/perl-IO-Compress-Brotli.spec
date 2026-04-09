# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Compress-Brotli
Version:        0.019
Release:        %autorelease
Summary:        Write Brotli buffers/streams
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Compress-Brotli
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/T/TI/TIMLEGGE/IO-Compress-Brotli-%{version}.tar.gz

# Use pkgconfig instead of bundled libbrotli
Patch0:         0001-use-system-brotli.patch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
#BuildRequires:  perl(Alien::cmake3)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Time::HiRes)
# Manual
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  perl(ExtUtils::PkgConfig)

%description
IO::Compress::Brotli is a module that compressed Brotli buffers and
streams. Despite its name, it is not a subclass of IO::Compress::Base
and does not implement its interface. This will be rectified in a
future release.

%prep
%setup -q -n IO-Compress-Brotli-%{version}
%patch -P 0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
