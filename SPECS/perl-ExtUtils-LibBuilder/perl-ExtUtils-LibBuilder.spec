# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-ExtUtils-LibBuilder
Version:        0.09
Release:        %autorelease
Summary:        ExtUtils::LibBuilder Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-LibBuilder
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/A/AM/AMBS/ExtUtils-LibBuilder-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.23
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

%description
Some Perl modules need to ship C libraries together with their Perl code.
Although there are mechanisms to compile and link (or glue) C code in your
Perl programs, there isn't a clear method to compile standard, self-
contained C libraries.

%prep
%setup -q -n ExtUtils-LibBuilder-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
