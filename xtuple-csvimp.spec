Name: xtuple-csvimp
Version: 0.5.0
Release: 1%{?dist}
Summary: xTuple data import utility
License: CPAL
Url: http://www.xtuple.org/DataImportTool
Source: https://github.com/xtuple/csvimp/archive/v%version.tar.gz
BuildRequires: qt-devel
BuildRequires: xtuple-openrpt-devel

%global _docdir_fmt %{name}

%description
A tool designed to import Comma Separated Value (CSV) files into the
database for the xTuple Applications (PostBooks and OpenMFG).

%package devel
Summary: CSVImp development files
Requires: qt-devel
Requires: libdmtx-devel
Requires: xtuple-openrpt-devel

%description devel
A tool designed to import Comma Separated Value (CSV) files into the
database for the xTuple Applications (PostBooks and OpenMFG).
This package provides the header files used by developers.

%prep
%setup -q  -n csvimp-%{version}

%build
export HARDCODE_APPLICATION_DIR='\"/usr/lib/csvimp\"'
export USE_SHARED_OPENRPT=1
export OPENRPT_HEADERS=/usr/include/openrpt
export OPENRPT_LIBDIR=%{_libdir}
#lrelease-qt4 */*/*.ts */*.ts
qmake-qt4 .
make %{?_smp_mflags}

%install
# make install doesn't do anything for this qmake project so we do
# the installs manually
#make INSTALL_ROOT=%{buildroot} install
rm -f %{buildroot}%{_libdir}/lib*.a
mkdir -p %{buildroot}%{_bindir}
install csvimp %{buildroot}%{_bindir}
mkdir -p %{buildroot}/usr/lib/csvimp/plugins
install plugins/libcsvimpplugin.so %{buildroot}/usr/lib/csvimp/plugins
mkdir -p %{buildroot}%{_includedir}/csvimp
find . -name '*.h' -exec install -m 0644 -D {} %{buildroot}%{_includedir}/csvimp/{} \;

%post

%postun

%files 
%{_bindir}/*
%dir /usr/lib/csvimp
%dir /usr/lib/csvimp/plugins
/usr/lib/csvimp/plugins/libcsvimpplugin.so

%files devel
%dir %{_includedir}/csvimp/
%{_includedir}/csvimp/*

%changelog
* Wed Feb 25 2015 Daniel Pocock <daniel@pocock.pro> - 0.5.0-1
- Initial RPM packaging.

