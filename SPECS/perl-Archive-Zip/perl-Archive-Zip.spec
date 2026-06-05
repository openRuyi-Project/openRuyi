# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Archive-Zip
Version:        1.68
Release:        %autorelease
Summary:        Provide an interface to ZIP archive files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Archive-Zip
#!RemoteAsset:  sha256:984e185d785baf6129c6e75f8eb44411745ac00bf6122fb1c8e822a3861ec650
Source0:        https://www.cpan.org/authors/id/P/PH/PHRED/Archive-Zip-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.017
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Local)

Requires:       perl(Compress::Raw::Zlib) >= 2.017
Requires:       perl(File::Spec) >= 0.80

%description
The Archive::Zip module allows a Perl program to create, manipulate, read,
and write Zip archive files.

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
