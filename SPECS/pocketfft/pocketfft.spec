# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit0 076cb3d2536b7c5d0629093ad886e10ac05f3623
%global shortcommit0 076cb3d
%global date0 20260211

%global pocketfft_description %{expand:
PocketFFT for C++
=================

This is a heavily modified implementation of FFTPack [1,2], with the following
advantages:

- Strictly C++11 compliant
- More accurate twiddle factor computation
- Worst case complexity for transform sizes with large prime factors is
  `N*log(N)`, because Bluestein's algorithm [3] is used for these cases.
- Supports multidimensional arrays and selection of the axes to be transformed.
- Supports `float`, `double`, and `long double` types.
- Supports fully complex and half-complex (i.e. complex-to-real and
  real-to-complex) FFTs. For half-complex transforms, several conventions for
  representing the complex-valued side are supported (reduced-size complex
  array, FFTPACK-style half-complex format and Hartley transform).
- Supports discrete cosine and sine transforms (Types I-IV)
- Makes use of CPU vector instructions when performing 2D and higher-dimensional
  transforms, if they are available.
- Has a small internal cache for transform plans, which speeds up repeated
  transforms of the same length (most significant for 1D transforms).
- Has optional multi-threading support for multidimensional transforms
}

Name:           pocketfft
Version:        0+git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        C++ header for FFT
License:        BSD-3-Clause
URL:            https://github.com/mreineck/%{name}
#!RemoteAsset
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# Only a header
BuildArch:      noarch

BuildRequires:  gcc-c++

%description
%{pocketfft_description}

%package        devel
Summary:        C++ header for FFT
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{pocketfft_description}

%prep
%autosetup -n %{name}-%{commit0}

%check
g++ pocketfft_demo.cc -o test
./test

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 pocketfft_hdronly.h %{buildroot}%{_includedir}

%files devel
%doc README.md
%license LICENSE.md
%{_includedir}/pocketfft_hdronly.h

%changelog
%autochangelog
