# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-TrailingSpace
Version:        0.0601
Release:        %autorelease
Summary:        Test for trailing space in source files
License:        MIT
URL:            https://metacpan.org/dist/Test-TrailingSpace
#!RemoteAsset:  sha256:abb8ce74483a63d73fe1ef603b7ce0a6d47c98ede731955d735784fad1dc4fcc
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-TrailingSpace-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(File::Find::Object::Rule) >= 0.0301
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::TreeCreate)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(autodie)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(File::Find::Object::Rule) >= 0.0301
Requires:       perl(Test::More) >= 0.88

%description
This module is used to test for lack of trailing space. See the synopsis
for more details.

%prep
%setup -q -n Test-TrailingSpace-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README weaver.ini
%license LICENSE

%changelog
%autochangelog
