# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Copy-Recursive-Reduced
Version:        0.008
Release:        %autorelease
Summary:        Recursive copying of files and directories
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Copy-Recursive-Reduced
#!RemoteAsset:  sha256:462bd66bf55e74b78f29ebdc9626af622d4f0115b5191b03167e82164db98f5a
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/File-Copy-Recursive-Reduced-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::More) >= 0.44

%description
File::Copy::Recursive::Reduced provides recursive file and directory copying
for Perl toolchain code.

%files -f %{name}.files
%doc Changes README Todo
%license LICENSE

%changelog
%autochangelog
