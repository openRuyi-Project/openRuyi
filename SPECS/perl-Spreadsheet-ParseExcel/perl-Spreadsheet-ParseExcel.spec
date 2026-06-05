# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Spreadsheet-ParseExcel
Version:        0.66
Release:        %autorelease
Summary:        Read information from an Excel file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Spreadsheet-ParseExcel
#!RemoteAsset:  sha256:bfd76acfba988601dc051bda73b4bb25f6839a006dd960b6a7401c249245f65b
Source0:        https://www.cpan.org/authors/id/J/JM/JMCNAMARA/Spreadsheet-ParseExcel-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::RC4)
BuildRequires:  perl(Digest::Perl::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(OLE::Storage_Lite) >= 0.19
BuildRequires:  perl(Scalar::Util)

Requires:       perl(OLE::Storage_Lite) >= 0.19

%description
The Spreadsheet::ParseExcel module can be used to read information from
Excel 95-2003 binary files.

%files -f %{name}.files
%doc Changes CP932Excel.map README README_Japan.htm

%changelog
%autochangelog
