from os import sys, path

if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from watson_bots_communicator.processor import main
    main()
