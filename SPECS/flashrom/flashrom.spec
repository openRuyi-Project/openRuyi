# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# For whatever reason our LTO options will cause the following testcase to fail with SIGSEGV:
# flashrom:cmocka test flashrom
# Disabling it for now
%global _lto_cflags %{nil}

Name:           flashrom
Version:        1.8.0
Release:        %autorelease
Summary:        Utility for identifying, reading, writing, verifying and erasing flash chips
License:        GPL-2.0-only
URL:            https://www.flashrom.org/
VCS:            git:https://review.coreboot.org/flashrom
#!RemoteAsset:  sha256:654c9c61745c250cd3b5ccd0e56fc43ee76980f92a5e078420420639d66975a2
Source:         https://download.flashrom.org/releases/flashrom-v%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  --auto-features=auto

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  python-sphinx
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libftdi1)
BuildRequires:  pkgconfig(libjaylink)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  linux-headers

Requires:       libftdi
Requires:       libjaylink
Requires:       libusb
Requires:       pciutils
Requires:       openssl

%description
%{name} is a utility for identifying, reading, writing, verifying and erasing flash chips.
It is designed to flash BIOS/EFI/coreboot/firmware/optionROM images on mainboards,
network/graphics/storage controller cards, and various other programmer devices.

%package        bash-completion
Summary:        Bash tab-completion for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bash-completion

%description    bash-completion
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%package	    doc
Summary:	    Documentation for ${name}

%description	doc
%{summary}.

%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
%{summary}.

%install -a
rm -f %{buildroot}%{_docdir}/%{name}/html/.buildinfo

%files
%{_sbindir}/flashrom
%{_libdir}/libflashrom.so.1.0.0
%{_libdir}/libflashrom.so.1

%files bash-completion
%{_datadir}/bash-completion/completions

%files devel
%{_includedir}/libflashrom.h
%{_libdir}/libflashrom.so
%{_libdir}/pkgconfig/flashrom.pc

%files doc
%{_docdir}/%{name}/html/*
%{_mandir}/man8/%{name}.8.*

%files static
%{_libdir}/libflashrom.a

%changelog
%autochangelog
