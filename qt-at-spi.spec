
Name:    qt-at-spi
Version: 0.3.1
Release: 5%{?dist}
Summary: Qt plugin that bridges Qt's accessibility API to AT-SPI2 

License: LGPLv2+
URL:     https://gitorious.org/qt-at-spi
%if 0%{?snap:1}
# git clone git://gitorious.org/qt-at-spi/qt-at-spi.git; cd qt-at-spi
# git archive master --prefix=qt-at-spi/ | xz > qt-at-spi-%{snap}.tar.xz
Source0: qt-at-spi-%{snap}.tar.xz
%else
# https://gitorious.org/qt-at-spi/qt-at-spi/archive-tarball/v%{version}
Source0: qt-at-spi-qt-at-spi-v%{version}.tar.gz
%endif
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Source1: qt-at-spi.sh

BuildRequires: pkgconfig(atspi-2)
BuildRequires: pkgconfig(QtDBus) >= 4.8.0
BuildRequires: pkgconfig(QtGui) pkgconfig(QtXml)

%{?_qt4:Requires: %{_qt4}%{?_isa} >= %{_qt4_version}}

%description
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.


%prep
%setup -q -n %{name}-%{name}

install -m644 -p %{SOURCE1} .


%build
%{_qt4_qmake}
make %{?_smp_mflags}

# build docs
pushd doc
qdoc3 qatspi.qdocconf
popd


%install
make install INSTALL_ROOT=%{buildroot}


%files
%doc LICENSE README
%doc qt-at-spi.sh
%dir %{_qt4_plugindir}/accessiblebridge/
%{_qt4_plugindir}/accessiblebridge/libqspiaccessiblebridge.so

%files doc
# install these under %{_qt4_docdir}? --rex
%doc doc/html/*


%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Rex Dieter <rdieter@fedoraproject.org> 0.3.1-3
- include sample qt-at-spi.sh shell fragment

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Jaroslav Reznik <jreznik@redhat.com> 0.3.1-1
- 0.3.1, fixes accessing invalid objects

* Thu Apr 12 2012 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-1
- 0.3.0

* Tue Apr 03 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2-2
- License: LGPLv2+
- -doc subpkg

* Wed Mar 14 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2-1
- 0.2

* Thu Jan 05 2012 Rex Dieter <rdieter@fedoraproject.org> 0.1.1-1
- 0.1.1

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1-1
- 0.1 release

* Tue Oct 25 2011 Rex Dieter <rdieter@fedoraproject.org> 0.0-0.1.20111025
- first try


