# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Spreadsheet-WriteExcel
Version:        2.40
Release:        %autorelease
Summary:        Write to a cross-platform Excel binary file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Spreadsheet-WriteExcel
#!RemoteAsset:  sha256:e356aad6866cf135731268ee0e979a197443c15a04878e9cf3e80d022ad6c07e
Source0:        https://www.cpan.org/authors/id/J/JM/JMCNAMARA/Spreadsheet-WriteExcel-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(OLE::Storage_Lite) >= 0.19
BuildRequires:  perl(Parse::RecDescent)

Requires:       perl(OLE::Storage_Lite) >= 0.19

%description
The Spreadsheet::WriteExcel Perl module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a workbook
and formatting can be applied to cells. Text, numbers, formulas,
hyperlinks, images and charts can be written to the cells.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
