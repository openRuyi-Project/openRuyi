# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Mozilla-PublicSuffix
Version:        1.0.7
Release:        %autorelease
Summary:        Get a domain name's public suffix via the Mozilla Public Suffix List
License:        MIT
URL:            https://metacpan.org/dist/Mozilla-PublicSuffix
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/T/TO/TOMHUKINS/Mozilla-PublicSuffix-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)

%description
This module provides a single function that returns the public suffix of a
domain name by referencing a parsed copy of Mozilla's Public Suffix List.
From the official website at http://publicsuffix.org/:

%prep
%setup -q -n Mozilla-PublicSuffix-v%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes effective_tld_names.dat README

%changelog
%autochangelog
