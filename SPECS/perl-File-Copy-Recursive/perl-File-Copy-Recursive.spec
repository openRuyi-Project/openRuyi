# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Copy-Recursive
Version:        0.45
Release:        %autorelease
Summary:        Perl extension for recursively copying files and directories
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Copy-Recursive
#!RemoteAsset:  sha256:d3971cf78a8345e38042b208bb7b39cb695080386af629f4a04ffd6549df1157
Source0:        https://www.cpan.org/authors/id/D/DM/DMUEY/File-Copy-Recursive-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)

%description
This module copies and moves directories recursively (or single files,
well... singley) to an optional depth and attempts to preserve each file or
directory's mode.

%files -f %{name}.files
%doc Changes README README.md

%changelog
%autochangelog
