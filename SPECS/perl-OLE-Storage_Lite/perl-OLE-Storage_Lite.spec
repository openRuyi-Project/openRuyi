# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-OLE-Storage_Lite
Version:        0.24
Release:        %autorelease
Summary:        Simple Class for OLE document interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/OLE-Storage_Lite
#!RemoteAsset:  sha256:71c3b6ef082176c9585e620dd48f0f4782c282be73f2a653ea4b618f757bb3fd
Source0:        https://www.cpan.org/authors/id/J/JM/JMCNAMARA/OLE-Storage_Lite-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
OLE::Storage_Lite allows you to read and write an OLE structured file.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
